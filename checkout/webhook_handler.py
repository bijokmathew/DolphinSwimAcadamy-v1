"""
Webhook Handler module for handling the
webhook event from stripe
"""

# ------------------------------------------------
# 3rd party
from django.http import HttpResponse

# internal

# -------------------------------------------------


class StripeWHHandler:
    """
    Handle the webhook event from stripe
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        default handler for unhandled webhook
        events from stripe
        """
        return HttpResponse(
            content=f"Unhandled webhook recieved: {event['type']}",
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook
        event from stripe
        """
        return HttpResponse(
            content=f"Webhook success recieved: {event['type']}",
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.payment_failed webhook
        event from stripe
        """
        return HttpResponse(
            content=f"Webhook failed recieved: {event['type']}",
            status=200
        )