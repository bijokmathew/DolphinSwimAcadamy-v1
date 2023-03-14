"""
 Module bag_tools for bag template tags
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django import template

# internal
# ------------------------------------------------------------------

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    This function calculate the total price
    of the product
    """
    return price*quantity
