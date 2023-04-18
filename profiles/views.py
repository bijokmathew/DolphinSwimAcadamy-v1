"""
 Module view for profiles app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import (
    render,
    get_object_or_404,
)

# internal
from .forms import UserProfileForm
from checkout.models import Order
from .models import UserProfile
# ------------------------------------------------------------------


@login_required
def user_profile(request):
    """
    This function return the template and user profile data
    to display user profile
    Args:
        request (object)
    Returns:
       Retun template and context
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all()
    template = 'profiles/profile.html'

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context=context)


def order_history(request, order_number):
    """
    This function return specific order of the
    specific user
    Args:
        request (object, order_number)
    Returns:
        Retun template and context
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
        )
    )
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile_page': True
    }
    return render(request, template, context=context)
