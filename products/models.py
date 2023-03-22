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


# class Image(models.Model):
#     """
#     Image model class
#     This model contain all the product
#     image name and url
#     """
#     alternative_text = models.CharField(
#         max_length=256
#     )
#     image = models.ImageField(
#         upload_to='products/',
#         null=True,
#         blank=True
#     )


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
    category = models.ManyToManyField(
        Category
    )
    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=False
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

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

    def get_categories(self):
        return "\n".join([cat.name for cat in self.category.all()])


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
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        This functions returns the atribute name
        and its value
        """
        return f"{self.attribute.name} : {self.value}"

    def get_attribute_name(self):
        """
        This function returns the attribue name 
        """
        return self.attribute.name


class Inventory(models.Model):
    """
    Class for inventory model
    This model contains products retated to different
    attribute
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='inventory_product',
    )
    attribute_value = models.ManyToManyField(
        AttributeValue
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    units = models.PositiveIntegerField(
        default=0
    )

    def generate_sku():
        """
        This function generate unique sku number
        for each inventory item
        """
        unique = True
        while unique:
            sku_ref = 'pp'+str(random.randint(1010201, 1011031))+'de'
            if not Inventory.objects.filter(sku=sku_ref):
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
        """
        This function return list of all attribute values
        belongs to the specific product
        """
        print("aa",  self.attribute_value.all()[0].get_attribute_name())
        print("bb", list([a for a in self.attribute_value.all()]))
        return list([a.value for a in self.attribute_value.all()])

    def get_attributes_name(self):
        """
        This function return list of all attribute name
        belongs to the attribute value
        """
        return list([a.get_attribute_name() for a in self.attribute_value.all()])


# class StockControl(models.Model):
#     """
#     StockControl model class
#     This model contains quatity of the
#     products
#     """
#     inventory = models.OneToOneField(
#         Inventory,
#         on_delete=models.CASCADE
#     )
      
#     last_checked = models.DateTimeField(
#         auto_now=True,
#         editable=False
#     )
