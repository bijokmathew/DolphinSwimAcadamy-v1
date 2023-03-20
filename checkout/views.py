"""
 Module view for checkout app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages

# internal
from .forms import OrderForm
# ------------------------------------------------------------------


def checkout(request):
    """
    This function processes the checkout: the cart contents, user info and
    the payment, validating it in the process.
    Credit: Boutique Ado project, Code Institute.
    Args:
        request (object)
    Returns:
        The request object, the checkout template and the context.
    """
    bag = request.session.get('bag', {})
    # prevet user to go to checkout by expliciltly typing checkout url
    if not bag:
        messages.error(request, "There is nothing in your bag at the momemt!")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context=context)
