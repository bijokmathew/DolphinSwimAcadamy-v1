"""
Checkout module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.contrib import admin
from django.urls import path, include

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path('', views.checkout, name='checkout'),
]