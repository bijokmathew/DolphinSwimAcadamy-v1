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
    print("view bag")
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add the quatity of the sepecified item requested by
    the shopper to the shopper bag
    """
    sku = request.POST.get('sku')
    item = get_object_or_404(Inventory, sku=sku)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect-url')
    bag = request.session.get('bag', {})

    if sku in list(bag.keys()):
        bag[sku] += quantity
        messages.success(
            request,
            f'Updated {item.product.name} quantity to {bag[sku]}',
            extra_tags='from_bag_view'
        )
    else:
        bag[sku] = quantity
        messages.success(
            request,
            f'Added {item.product.name} to your shopping cart',
            extra_tags='from_bag_view'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quatity of the specific product
    """
    sub_product = get_object_or_404(Inventory, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product_size = request.session.get('product_size')
    print("adjust_bag product_size= ", product_size)

    if quantity > 0:
        bag[sub_product.sku] = quantity
        messages.success(
            request,
            f"Updated {sub_product.product.name}quantity"
            "to {bag[sub_product.sku]}",
            extra_tags='from_bag_view'
        )
    else:
        bag.pop(sub_product.sku)
        messages.success(
            request,
            f"Removed {sub_product.product.name} from your bag",
            extra_tags='from_bag_view'
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove sepecified product from the bag
    """
    print('remove_from_bag')
    try:
        sub_product = get_object_or_404(Inventory, pk=item_id)
        bag = request.session.get('bag', {})
        size = request.POST.get('product_size')
        bag.pop(sub_product.sku)
        messages.success(
            request,
            f"Removed {sub_product.product.name} from your bag",
            extra_tags='from_bag_view'
        )
        request.session['bag'] = bag
        return redirect('view_bag')
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
