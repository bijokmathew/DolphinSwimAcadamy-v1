from django.contrib import admin
from .models import UserProfile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'default_phone_number',
        'default_country', 'default_postcode', 'default_town_or_city', 'default_street_address1',
        'default_street_address2', 'default_county',
    )


admin.site.register(UserProfile, ProfileAdmin)
