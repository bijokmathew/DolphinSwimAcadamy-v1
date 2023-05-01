"""
 Context module for bag app 
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal


# internal
from products.models import Inventory

# ------------------------------------------------------------------


def bag_contents(request):
    """
    Add shopping bag items, quantity, total etc
     from session to context processor
    """
    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})
    for sku, quantity in bag.items():
        sub_product = get_object_or_404(Inventory, sku=sku)
        total += sub_product.product.price * quantity
        product_count += quantity
        bag_items.append(
            {
                'sub_product': sub_product,
                'total': total,
                'quantity': quantity
            }
        )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = round(
            total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100), 2
        )
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'total': total,
        'grand_total': grand_total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'bag_items': bag_items,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'product_count': product_count
    }

    return context
