"""
Form module for Course models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django import forms

# internal
from .models import Course
# ------------------------------------------------------------------


class CorseForm(forms.ModelForm):
    """
    Modelform for Course model
    """

    class Meta:
        model = Course
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        """
        override the init method to customize the
        course form
        """
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
