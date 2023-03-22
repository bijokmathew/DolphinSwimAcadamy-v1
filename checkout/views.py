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
from .models import Order, OrderLineItem
from bag.contexts import bag_contents
from products.models import Product
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
        The request object, the checkout template, checkout_success template 
        and the context.
    """
    # Get the stripe secret and public key from settings
    stripePublicKey = settings.STRIPE_PUBLIC_KEY
    clientSecret = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    # prevet user to go to checkout by expliciltly typing checkout url
    if not bag:
        messages.error(request, "There is nothing in your bag at the momemt!")
        return redirect(reverse('products'))
    if request.method == 'POST':
        form_data = {
            "full_name": request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                                product_size=size
                            )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the product in your bag \
                        was not found in our database. \
                        Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))
        else:
            messages.error(request, "There was an error with your form. \
                Please double check with your information.")
    else:
        current_bag = bag_contents(request)
        stripe.api_key = clientSecret
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
    if not stripePublicKey:
        messages.warning(request, "Stripe public key is missing. \
                          Did you forget to set it in to your enviroment")
    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripePublicKey,
        'client_secret': intent.client_secret
    }
    return render(request, template, context=context)


def checkout_success(request, order_number):
    """
    Handle checkout success message
    Args:
        request (object, order_number)
    Returns:
        The request object, the checkout_success template and order.
    """
    save_info = request.session['save_info']
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}")
    if 'bag' in request.session:
        del request.session['bag']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }
    return render(request, template, context=context)