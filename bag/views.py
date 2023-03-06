"""
 Module view for bag app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render

# internal
# ------------------------------------------------------------------


def view_bag(request):
    """
    This view render and return the bag conetnts page
    """
    return render(request, 'bag/bag.html')
