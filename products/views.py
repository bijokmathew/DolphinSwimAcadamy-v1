"""
 Module view for product app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q, Max
from django.views import generic

# internal
from .models import Inventory, Category, Product
from .forms import ProductForm
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

        if 'category' in request.GET:
            category_list = request.GET['category'].split(',')
            products = Product.objects.filter(category__slug__in=category_list)
            print('category_list =', category_list)
            category_list = Category.objects.filter(slug__in=category_list)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria !!"
                )
                redirect(reverse('products'))
            else:
                queries = (
                    Q(name__icontains=query) | Q(description__icontains=query)
                )
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
    the product list
    Args:
        request (object): HTTP request object.
    Returns:
        Render of products page with context
    """
    product = get_object_or_404(Product, id=product_id)
    print("BKM p-->", product)
    sub_products = product.inventories.all()
    print("BKM sub--", sub_products)
    product_attr = {}
    has_size = False
    has_color = False
    has_style = False
    for sub in sub_products:
        print("sub-val", sub.product.name, sub.size, sub.units)

    context = {
        'product': product,
        'sub_products': sub_products,
    }
    return render(request, 'products/product_detail.html', context=context)


@login_required
def product_add(request):
    """
    This function create a view for adding the product
    to the database
    """
    if not request.user.is_superuser:
        messages.error(request, f"Sorry, You are not autherized to perform this action")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request,
                f"Successfully {product.name} added to the store"
            )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                f"Sorry!, Failed to add the product. Please ensure the\
                 form is valid"
            )
    else:
        form = ProductForm()
    template = 'products/product_add.html'

    context = {
        'form': form
    }
    return render(request, template, context=context)


@login_required
def product_edit(request, product_id):
    """
    A view to edit the product from the
    the product list
    credit from code institute Boutique Ado
    Args:
        request (object): HTTP request object
        and product id.
    Returns:
        Render of product edit page with context
    """
    if not request.user.is_superuser:
        messages.error(request, f"Sorry, You are not autherized to perform this action")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated the product")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                f"Failed to update the product.Plesae ensure the form is valid"
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")
    template = 'products/product_edit.html'
    context = {
        'product': product,
        'form': form
    }
    return render(request, template, context=context)


@login_required
def delete_product(request, product_id):
    """
     A view to delete the product from the
    the product list
    credit from code institute Boutique Ado
    Args:
        request (object): HTTP request object
        and product id.
    Returns:
        Delete the product and return to ptoduct list
    """
    if not request.user.is_superuser:
        messages.error(request, f"Sorry, You are not autherized to perform this action")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"Product deleted!")
    return redirect(reverse('products'))
