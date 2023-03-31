"""
Profiles module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.urls import path

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
]
