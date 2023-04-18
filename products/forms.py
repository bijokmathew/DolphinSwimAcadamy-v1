"""
Form module for products related models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django import forms

# internal
from .widgets import CustomClearableFileInput
from .models import Product, Category
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
            field.widget.attrs['class'] = 'border-black rounded-0'

    category = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )