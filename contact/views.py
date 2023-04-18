"""
 Module view for Contact app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404, reverse, redirect

# internal
from profiles.models import UserProfile
from .forms import ContactForm
# ------------------------------------------------------------------


def contact(request):
    """
    This function process post request from contact.
    For get request return the contact view 
    Args:
        request (object)
    Returns:
       Retun the contact template
    """
    # for tracking whether the user contacted or not
    is_contacted = False
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            is_contacted = True
    else:
        # fill the form with saved profile
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                print("saved profile contact, addrees",  user_profile.default_street_address1)
                contact_form = ContactForm(initial={
                    'full_name': user_profile.user.get_full_name(),
                    'email': user_profile.user.email,
                    'phone_number': user_profile.default_phone_number,
                    'street_address': user_profile.default_street_address1,
                    'town_or_city': user_profile.default_town_or_city,
                    'county': user_profile.default_county,
                    'postcode': user_profile.default_postcode,
                    'country': user_profile.default_country,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    template = 'contact/contact.html'

    context = {
        'form': contact_form,
        'is_contacted': is_contacted
    }
    return render(request, template, context=context)
