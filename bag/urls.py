"""
Bag module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.contrib import admin
from django.urls import path, include

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust_bag/<item_id>', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]