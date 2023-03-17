"""
Signals modules for checkout app
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# internal
from .models import OrderLineItem
# ------------------------------------------------------------------


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order_total, grand_total fields of order model
    when OrderLine model created/updated
    """
    instance.Order.update_order_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order_total, grand_total fields of order model
    when OrderLine model deleted
    """
    instance.Order.update_order_total()
