"""
Webhook Handler module for handling the
webhook event from stripe
"""

# ------------------------------------------------
# 3rd party
from django.http import HttpResponse
import stripe
import json
import time

# internal
from .models import Order, OrderLineItem
from products.models import Product

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
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        saveInfo = intent.metadata.save_info

        # Get charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        shipping_details = intent.shipping
        billing_details = stripe_charge.billing_details
        grand_total = round(stripe_charge.amount / 100, 2)
        print('handle_payment_intent_succeeded grand_total ==', grand_total, stripe_charge.amount)
        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        attempt = 1
        order_exits = False
        while attempt < 5:
            try:
                print('handle_payment_intent_succeeded inside try')
                order = Order.objects.get(
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    country__iexact=shipping_details.address.country,
                    county__iexact=shipping_details.address.state,
                    phone_number__iexact=shipping_details.phone,
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    original_bag=bag
                )
                print('handle_payment_intent_succeeded inside try-val')
                order_exits = True
                break
            except Order.DoesNotExist:
                print('handle_payment_intent_succeeded inside DoesNotExist-val')
                order_exits = False
                attempt += 1
                time.sleep(1)
            except Exception as e:
                print('handle_payment_intent_succeeded inside Exception e==', e)
        if order_exits:
            print('handle_payment_intent_succeeded oredr exist')
            return HttpResponse(
                content=f'Webhook success event recieved: {event["type"]} '
                        '| Success: Verified order already in database',
                status=200
            )
        else:
            print('handle_payment_intent_succeeded inside DoesNotExist--false')
            order = None
            try:
                order = Order.objects.create(
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    country=shipping_details.address.country,
                    county=shipping_details.address.state,
                    phone_number=shipping_details.phone,
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                print('handle_payment_intent_succeeded DoesNotExist--false order created')
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['item_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                product_size=size,
                                quantity=quantity,
                            )
                            order_line_item.save()
                    print('handle_payment_intent_succeeded inside order-line created')
            except Exception as e:
                print('handle_payment_intent_succeeded inside order created Exception-', e)
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} |'
                            ' ERROR: {e}',
                    status=200
                )
        return HttpResponse(
           content=f'Webhook succ recieved: {event["type"]}'
                   '| Success: created order in webhook ',
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
