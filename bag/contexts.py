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
    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        if not isinstance(item_data, int):
            for size, quantity in item_data['item_by_size'].items():
                total += product.price * quantity
                product_count += quantity
                bag_items.append(
                    {
                        'product': product,
                        'size': size,
                        'item_id': item_id,
                        'quantity': quantity
                    }
                )
        else:
            total += product.price * item_data
            product_count += item_data
            bag_items.append(
                {
                    'product': product,
                    'item_id': item_id,
                    'quantity': item_data
                }
            )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = round(total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100), 2)
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
