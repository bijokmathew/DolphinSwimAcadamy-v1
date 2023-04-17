"""
 Module view for Contact app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404, reverse, redirect

# internal
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
    template = 'contact/contact.html'
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, template, context=context)
