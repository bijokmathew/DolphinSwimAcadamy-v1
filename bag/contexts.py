"""
 Context module for bag app 
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404

# internal
from products.models import Product

# ------------------------------------------------------------------


def bag_contents(request):
    """
    Add shopping bag items, quantity, total etc
     from session to context processor
    """
    print("bag_contents")
    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price * quantity
        product_count += quantity
        bag_items.append(
            {
                'product': product,
                'item_id': item_id,
                'quantity': quantity
            }
        )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
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
