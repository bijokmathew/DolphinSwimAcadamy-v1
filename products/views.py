"""
 Module view for product app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    A view to show product detail from the
    the profuct list
    """
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context=context)
