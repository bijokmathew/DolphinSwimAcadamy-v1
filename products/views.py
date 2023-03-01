"""
 Module view for product app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render

# internal
from .models import Inventory
# ------------------------------------------------------------------


def all_products(request):
    """
    A view to show all products, including
    sorting and searching queries
    """
    products = Inventory.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context=context)
