"""
Webhooks module for re-direct the 
webhook events to suitable webhook
handler

"""

# ------------------------------------------------
# 3rd party
from django.http import HttpResponse

# internal
from .webhook_handler import StripeWHHandler

# -------------------------------------------------


def webhook(self, request):
    """
    Listen for webhook events from the stripe
    """
    # setup
    wh_secret = settings.STRIPE_WEBHOOK_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
         )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # Generic exception
        return HttpResponse(content=e, status=400)

    # set up a webhook handler
    handler = StripeWHHandler(request)

    # Map webhook events to relevant handler
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed
    }

    # Get the type of webhook event from stripe
    event_type = event['type']
    # If there is handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)
    # Call the event handler with the event
    response = event_handler(event)
    return response
