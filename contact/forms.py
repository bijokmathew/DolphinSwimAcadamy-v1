"""
Form modules for Contact app
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django import forms

# internal
from .models import Contact
# ------------------------------------------------------------------


class ContactForm(forms.ModelForm):
    """
    Create a form for Contacting the company
    """
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        override default __init__() method to provide
        placeholder, remove labels and set auto focus
        on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address': 'Street Address',
            'county': 'County'
        }
        for field in self.fields:
            if field != 'country' and field != 'subject' \
             and field != 'message':
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-ocean-blue rounded-0'
            self.fields[field].label = False
