"""
 Module view for About app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render

# internal

# ------------------------------------------------------------------


def about(request):
    """
    This function return the view for about page
    Args:
        request (object)
    Returns:
       Retun the about template
    """
    template = 'about/about.html'
    return render(request, template)