"""
 Module widget for Product app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.utils.translation import gettext_lazy as _
from django.forms.widgets import ClearableFileInput

# internal
# ------------------------------------------------------------------


class CustomClearableFileInput(ClearableFileInput):
    """
    This class customize the image field
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _()
    template_name = 'products/custom_widget_templates/customclearablefileinput.html'
