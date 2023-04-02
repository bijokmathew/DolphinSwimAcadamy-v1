"""
 Module view for profiles app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import (
    render,
    get_object_or_404,
)

# internal
from .forms import UserProfileForm
from checkout.models import Order
from .models import UserProfile
# ------------------------------------------------------------------


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
    form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all()
    template = 'profiles/profile.html'

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context=context)