"""
Checkout app related models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party

from django_countries.fields import CountryField
from django.conf import settings
from django.db.models import Sum
from django.db import models
import uuid

# internal

from profiles.models import UserProfile
from products.models import Product
# ------------------------------------------------------------------


class Order(models.Model):
    """
    This model handle all orders belongs
    to dolphinswimacadamy website
    """
    order_number = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        editable=False
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    country = CountryField(
        blank_label='Country*',
        null=False,
        blank=False
    )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    street_address2 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    county = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    date = models.DateField(
        auto_now_add=True
    )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )
    original_bag = models.TextField(
        blank=False,
        null=False,
        default=''
    )

    def __generate_order_number(self):
        """
        This method generate random uinique
        order number by using uuid
        """
        return uuid.uuid4().hex.upper()

    def update_order_total(self):
        """
        Calculate the total amount of each order,
        and grand total
        """
        self.order_total = self.lineItems.aggregate(
            Sum('lineItem_total'))['lineItem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total *\
                 settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the save method to update
        the order number if it has not set
        already
        """
        if not self.order_number:
            self.order_number = self.__generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Override the __str__() to return order number
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    This model holds all the products, quantity
    product size and total costs corresponding to
    each order
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='lineItems'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    quantity = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )
    product_size = models.CharField(
        max_length=4,
        blank=True,
        null=True
    )
    lineItem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=False,
        null=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the default save method to update the
        lineitem_total
        """
        self.lineItem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Override the __str__() to return order number and
        product sku
        """
        return f"SKU : {self.product.inventories.name} on order \
                       {self.order.order_number}"
