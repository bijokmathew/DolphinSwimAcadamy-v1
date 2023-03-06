"""
 Module view for product app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q, Max
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
    query = None
    category_list = None
    sort = None
    direction = None

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

        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sort_key == 'category':
                sort_key = 'max_category'
                products = products.annotate(max_category=Max('category'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                print("sort_ky==", sort_key)
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        if 'category' in request.GET:
            category_list = request.GET['category'].split(',')
            products = Product.objects.filter(category__slug__in=category_list)
            print('category_list =', category_list)
            category_list = Category.objects.filter(slug__in=category_list)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'categories': categories,
        'current_category': category_list,
        'current_sorting': current_sorting
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
