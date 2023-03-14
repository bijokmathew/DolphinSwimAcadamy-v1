"""
 Module view for bag app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, redirect, reverse, HttpResponse

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
    size = None
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    if size:
        if item_id in list(bag.keys()):
            print("nor==", bag[item_id]['item_by_size'])
            print("list ==", list(bag[item_id]['item_by_size']))
            if size in bag[item_id]['item_by_size']:
                bag[item_id]['item_by_size'][size] += quantity
            else:
                bag[item_id]['item_by_size'][size] = quantity
        else:
            bag[item_id] = {'item_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quatity of the specific product
    """
    print('adjust_bag nnnnnnnnnnnnnnnn')
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    if size:
        if quantity > 0:
            bag[item_id]['item_by_size'][size] = quantity
        else:
            del bag[item_id]['item_by_size'][size]
            if not bag[item_id]['item_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove sepecified product from the bag
    """
    print('remove_from_bag')
    try:
        bag = request.session.get('bag', {})
        size = None
        if 'product_size' in request.POST:
            size = request.POST.get('product_size')
        if size:
            del bag[item_id]['item_by_size'][size]
            if not bag[item_id]['item_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
