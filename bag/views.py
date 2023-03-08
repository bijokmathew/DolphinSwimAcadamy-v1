"""
 Module view for bag app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, redirect

# internal
# ------------------------------------------------------------------


def view_bag(request):
    """
    This view render and return the bag conetnts page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add the quatity of the sepecified item requested by
    the shopper to the shopper bag
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect-url')
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    request.session['bag'] = bag
    print('bag = ', request.session['bag'])
    return redirect(redirect_url)
