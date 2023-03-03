# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.contrib import admin
# internal
from .models import (
    Category,
    Product,
    Attribute,
    AttributeValue,
    Inventory,
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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for Product model
    """
    list_display = (
        'name',
        'description',
        'price',
        'get_categories',
        'slug',
    )
    prepopulated_fields = {
        "slug": ("name",)
    }


class AttributeValueInline(admin.TabularInline):
    """
    TabularInlineAdmin class for AttributeValue model
    """
    model = AttributeValue


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    """
    Admin class for Product model
    """
    list_display = (
        'name',
        'description',
    )
    inlines = (
        AttributeValueInline,
    )

# @admin.register(AttributeValue)
# class AttributeValueAdmin(admin.ModelAdmin):
#     """
#     Admin class for AttributeValue model
#     """
#     list_display = (
#         'attribute',
#         'value',
#     )


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    """
    Admin class for Inventory model
    """
    list_display = (
        'sku',
        'product',
        'get_attributes_values',
        'units',
        'date_added',
    )

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     """
#     Admin class for Image model
#     """
#     list_display = (
#         'inventory',
#         'image url',
#         'image',
#         'alternative text'
#     )


# @admin.register(StockControl)
# class StockControlAdmin(admin.ModelAdmin):
#     """
#     Admin class for StockControl model
#     """
#     list_display = (
#         'inventory',
#         'units',
#         'last checked'
#     )
