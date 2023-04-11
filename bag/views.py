"""
 Module view for bag app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages

# internal
from products.models import Product, Inventory
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
    sku = request.POST.get('sku')
    print("sku==", sku)
    item = get_object_or_404(Inventory, sku=sku)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect-url')
    bag = request.session.get('bag', {})

    if sku in list(bag.keys()):
        bag[sku] += quantity
        messages.success(
            request, f'Updated {item.product.name} quantity to {bag[sku]}'
        )
    else:
        bag[sku] = quantity
        messages.success(
            request, f'Added {item.product.name} to your shopping cart'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quatity of the specific product
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    if size:
        if quantity > 0:
            bag[item_id]['item_by_size'][size] = quantity
            messages.success(request, f"Updated size {size.upper()} {product.name} quantity to {bag[item_id]['item_by_size'][size]}")
        else:
            del bag[item_id]['item_by_size'][size]
            if not bag[item_id]['item_by_size']:
                bag.pop(item_id)
            messages.success(request, f"Removed size  {size.upper()} {product.name} from your bag")
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f"Updated {product.name}quantity to {bag[item_id]}")
        else:
            bag.pop(item_id)
            messages.success(request, f"Removed {product.name} from your bag")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove sepecified product from the bag
    """
    print('remove_from_bag')
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        size = None
        if 'product_size' in request.POST:
            size = request.POST.get('product_size')
        if size:
            del bag[item_id]['item_by_size'][size]
            if not bag[item_id]['item_by_size']:
                bag.pop(item_id)
            messages.success(request, f"Removed size  {size.upper()} {product.name} from your bag")
        else:
            bag.pop(item_id)
            messages.success(request, f"Removed {product.name} from your bag")
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
