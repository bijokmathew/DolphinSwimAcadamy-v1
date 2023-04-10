# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.contrib import admin
# internal
from .models import (
    Inventory,
    Category,
    Product,
    Size
)
# ------------------------------------------------------------------


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for Category model
    """
    list_display = (
        'name',
        'friendly_name',
    )
    prepopulated_fields = {
        "slug": ("name",)
    }


class InventoryInline(admin.TabularInline):
    """
    TabularInlineAdmin class for Inventory model
    """
    model = Inventory
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for Product model
    """
    list_display = (
        'name',
        'get_categories',
        'description',
        'get_product_size',
        'price',
        'is_active',
        'slug',
    )
    prepopulated_fields = {
        "slug": ("name",)
    }

    list_filter = (
        'category',
        'is_active',
    )

    search_fields = (
        'name',
        'category',
        'sku'
    )

    inlines = (
        InventoryInline,
    )


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    """
    Admin class for model size
    """
    list_display = (
        'name',
        'friendly_name'
    )
