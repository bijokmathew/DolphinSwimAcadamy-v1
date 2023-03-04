"""
 Module view for product app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic
from django.db.models import Q


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

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria !!"
                )
                redirect(reverse('products'))
            else:
              
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = Product.objects.filter(queries)

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
