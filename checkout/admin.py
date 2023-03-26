# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.contrib import admin

# internal
from .models import Order, OrderLineItem
# ------------------------------------------------------------------


class OrderLineItemInline(admin.TabularInline):
    """
    Display OrderLineItem model inside the parent model
    Order in Admin panel
    """
    model = OrderLineItem
    readonly_fields = ('lineItem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin model for the Order model
    """
    inlines = (OrderLineItemInline,)
    readonly_fields = (
                        'order_number', 'date',
                        'delivery_cost', 'order_total',
                        'grand_total', 'stripe_pid', 'original_bag',
                    )
    fields = (
                'order_number', 'full_name', 'email', 'phone_number',
                'country', 'postcode', 'town_or_city', 'street_address1',
                'street_address2', 'county', 'date', 'delivery_cost',
                'order_total', 'grand_total', 'stripe_pid', 'original_bag',
            )

    list_display = (
                        'order_number', 'date', 'full_name', 'order_total',
                        'delivery_cost', 'grand_total',
                    )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)