"""
Products app related models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.db import models

# internal
# ------------------------------------------------------------------


class Category(models.Model):
    """
    Category model
    This model describe all the categories related to the products
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        blank=True,
        null=True
    )
    slug = models.SlugField()

    def __str__(self):
        """
        This functions returs the category name
        """
        return self.name

    def get_friendly_name(self):
        """
        This functions returs the friendly category name
        """
        return self.friendly_name


class Product(models.Model):
    """
    Class for product model
    This model contains all the products
    """
    name = models.CharField(
        max_length=254,
        unique=True
    )
    description = models.TextField(
        max_length=1256,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    slug = models.SlugField()


class Inventory(models.Model):
    """
    Class for inventory model
    This model contains products retated to different
    attributes
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    attribute_values = models.ManyToManyField(AttributeValues)
    price = models.DecimalField()
    date_added = models.DateTimeField()
    sku = models.UUIDField()


class Attributes(models.Model):
    """
    Attributes model class
    This model describe the product attributes like 
    size, color etc
    """
    name = models.CharField(
        max_length=254
    )
    description = models.TextField()


class AttributeValues(models.Model):
    """
    ArrributeValues model class
    This model conatins values for attributes 
    like red, green for color etc
    """
    value = models.CharField(
        max_length=256
    )
    attributes = models.ForeignKey(
        Attributes,
        on_delete=models.SET_NULL
    )


class Image(models.Model):
    """
    Image model class
    This model contain all the product 
    image name and url
    """
    name = models.CharField(
        max_length=254
    )
    url = models.ImageField(
        upload_to='/products',
        blank=True,
        null=True
    )
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.SET_NULL
    )
    alternative_text = models.CharField(
        max_length=256
    )


class StockControl(models.Model):
    """
    StockControl model class
    This model contains quatity of the 
    products
    """
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.CASCADE
    )
    units = models.PositiveIntegerField()
    date_chacked = models.DateTimeField()
