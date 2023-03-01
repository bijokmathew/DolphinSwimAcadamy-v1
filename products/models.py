"""
Products app related models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
import random
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
    category = models.ManyToManyField(Category)
    # category = models.ForeignKey(
    #     Category,
    #     related_name='category',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )
    slug = models.SlugField()

    def __str__(self):
        """
        This functions returs the product name
        """
        return self.name


class Attribute(models.Model):
    """
    Attributes model class
    This model describe the product attribute like
    size, color etc
    """
    name = models.CharField(
        max_length=254
    )
    description = models.TextField()

    def __str__(self):
        """
        This functions returs the attribute name
        """
        return self.name


class AttributeValue(models.Model):
    """
    ArrributeValue model class
    This model conatins values for attribute
    like red, green for color etc
    """
    value = models.CharField(
        max_length=256
    )
    attribute = models.ForeignKey(
        Attribute,
        related_name='attribute',
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        This functions returs the atribute name
        and its value
        """
        return f"{self.attribute.name} : {self.value}"


class Inventory(models.Model):
    """
    Class for inventory model
    This model contains products retated to different
    attribute
    """
    product = models.ForeignKey(
        Product,
        related_name='product',
        on_delete=models.CASCADE
    )
    attribute_value = models.ManyToManyField(AttributeValue)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    is_active = models.BooleanField(
        default=False
    )

    def generate_sku():
        """
        This function generate unique sku number
        for each inventory item
        """
        unique = True
        while unique:
            sku_ref = 'pp'+str(random.randint(1010201, 1011031))+'de'
            unique = False
            if not Inventory.objects.filter(sku_ref=sku):
                unique = False
        return str(sku_ref)

    sku = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
        default=generate_sku,
    )

    def __str__(self):
        """
        This functions returs the product name
        """
        return self.product.name
    
    def get_attributes_values(self):
        return "\n".join([a.value for a in self.attribute_value.all()])


class Image(models.Model):
    """
    Image model class
    This model contain all the product 
    image name and url
    """
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE
    )
    alternative_text = models.CharField(
        max_length=256
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
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
    units = models.PositiveIntegerField(
        default=0
    )
    last_checked = models.DateTimeField(
        auto_now=True,
        editable=False
    )
