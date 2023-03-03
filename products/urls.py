"""
Home module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.contrib import admin
from django.urls import path, include

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
