# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.contrib import admin

# internal
from .models import Contact
# ------------------------------------------------------------------


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin model for contact model
    """
    list_display = (
        'full_name',
        'phone_number',
        'email',
        'subject',
        'message'
    )

    list_filter = (
        'full_name',
        'subject',
        'email'
    )

    search_fields = (
        'name',
        'phone_number',
        'subject'
    )
