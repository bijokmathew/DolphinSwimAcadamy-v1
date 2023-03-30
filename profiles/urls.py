"""
Profiles module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.contrib import admin

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
]
