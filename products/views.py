"""
 Module view for product app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render
from django.views import generic

# internal
from .models import Inventory, Category, Product
# ------------------------------------------------------------------


def all_products(request):
    """
    A view to show all products, including
    sorting and searching queries
    """
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/products.html', context=context)
