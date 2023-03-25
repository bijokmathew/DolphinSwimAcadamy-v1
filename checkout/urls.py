"""
Checkout module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.urls import path, include
from django.contrib import admin

# internal
from . import views
from .webhooks import webhook
# -------------------------------------------------

urlpatterns = [
    path(
        'checkout_success/<order_number>', views.checkout_success,
        name='checkout_success'
    ),
    path('', views.checkout, name='checkout'),
    path('wh/', webhook, name="webhook"),
]
