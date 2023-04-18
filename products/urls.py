"""
Product module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.contrib import admin
from django.urls import path, include

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path(
        '',
        views.all_products,
        name='products'
    ),
    path(
        'add/',
        views.product_add,
        name='product_add'
    ),
    path(
        '<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),
    path(
        'edit/<int:product_id>/',
        views.product_edit,
        name='product_edit'
    ),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    )
]
