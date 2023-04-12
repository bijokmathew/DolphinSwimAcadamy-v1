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
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
import stripe
import json

# internal
from profiles.forms import UserProfileForm
from .models import Order, OrderLineItem
from profiles.models import UserProfile
from products.models import Inventory
from bag.contexts import bag_contents
from .forms import OrderForm
# ------------------------------------------------------------------


@require_POST
def cache_checkout_data(request):
    """
    This function process post request from checkout.
    This funtion modify the paymentIntent with bag, saveIfo
    and user details
    Args:
        request (object)
    Returns:
       Retun the appropritae http response
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user
        })
        print("retun 200 cache_checkout_data save_info")
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry!, your payment cannot be processed \
            right now. Please try again later")
        return HttpResponse(
            content=e,
            status=400
        )


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
    print('request.method', request.method)
    print('stripePublicKey', settings.STRIPE_PUBLIC_KEY)
    print('clientSecret', settings.STRIPE_SECRET_KEY)
    if request.method == 'POST':
        form_data = {
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'phone_number': request.POST['phone_number'],
            'town_or_city': request.POST['town_or_city'],
            "full_name": request.POST['full_name'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'county': request.POST['county'],
            'email': request.POST['email'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print('order form is valid')
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for sku, quantity in bag.items():
                try:
                    sub_product = Inventory.objects.get(sku=sku)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=sub_product.product,
                        quantity=quantity
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    print('order form Product.DoesNotExist')
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
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = clientSecret
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        print("intent.client_secret", intent.client_secret)
        print('clientSecret', settings.STRIPE_SECRET_KEY)
    if not stripePublicKey:
        messages.warning(request, "Stripe public key is missing. \
                          Did you forget to set it in to your enviroment")
    # If user is authenticated, pre fill the checkout form with
    # saved profile info
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            print("saved profile checkout, addrees",  user_profile.default_street_address2)
            order_form = OrderForm(initial={
                'full_name': user_profile.user.get_full_name(),
                'email': user_profile.user.email,
                'phone_number': user_profile.default_phone_number,
                'street_address1': user_profile.default_street_address1,
                'street_address2': user_profile.default_street_address2,
                'town_or_city': user_profile.default_town_or_city,
                'county': user_profile.default_county,
                'postcode': user_profile.default_postcode,
                'country': user_profile.default_country,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        print("....else orderForm")
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
    # Add user profile to order model
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
        # save user profile
        if save_info:
            print("checkout_success default_street_address2 , save_info", order.street_address2, save_info)
            profile_data = {
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_phone_number': order.phone_number,
                'default_town_or_city': order.town_or_city,
                'default_postcode': order.postcode,
                'default_country': order.country,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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
