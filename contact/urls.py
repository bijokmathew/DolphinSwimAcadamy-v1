"""
Contact module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.urls import path

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path(
        '',
        views.contact,
        name='contact'
    ),
]
