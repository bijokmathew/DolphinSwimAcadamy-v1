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
]