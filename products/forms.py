"""
Form module for products models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django import forms

# internal
from .models import Product, Category, Inventory
from .widgets import CustomClearableFileInput
# ------------------------------------------------------------------


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return member.get_friendly_name()


class ProductForm(forms.ModelForm):
    """
    ModelForm for product model
    """

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'category',
            'description',
            'price',
            'is_active',
            'rating',
            'image'
        ]

    def __init__(self, *args, **kwargs):
        """
        override the init method to customize the
        product form
        """
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-ocean-blue rounded-0'

    category = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )


class InventoryForm(forms.ModelForm):
    """
    Model Form for Inventory model
    """
    class Meta:
        model = Inventory
        fields = ['units',]
