"""
 Module view for checkout app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages
from django.conf import settings

# internal
from bag.contexts import bag_contents
from .forms import OrderForm
import stripe
# ------------------------------------------------------------------


def checkout(request):
    """
    This function processes the checkout: the cart contents, user info and
    the payment, validating it in the process.
    Credit: Boutique Ado project, Code Institute.
    Args:
        request (object)
    Returns:
        The request object, the checkout template and the context.
    """
    # Get the stripe secret and public key from settings
    stripePublicKey = settings.STRIPE_PUBLIC_KEY
    clientSecret = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    current_bag = bag_contents(request)
    # prevet user to go to checkout by expliciltly typing checkout url
    if not bag:
        messages.error(request, "There is nothing in your bag at the momemt!")
        return redirect(reverse('products'))
    stripe.api_key = clientSecret
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripePublicKey,
        'client_secret': intent.client_secret
    }
    return render(request, template, context=context)
