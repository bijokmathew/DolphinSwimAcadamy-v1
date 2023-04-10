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
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        Args:
            self (object): self.
        Returns:
            The category friendly name string
        """
        return self.friendly_name


class Size(models.Model):
    """
    Size model class
    """
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    name = models.CharField(
        max_length=254
    )

    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def get_friendly_name(self):
        """
        Returns the size friendly name string
        Args:
            self (object): self.
        Returns:
            The size friendly name string
        """
        return self.friendly_name

    def __str__(self):
        """
        Returns the Size name string
        Args:
            self (object): self.
        Returns:
            The Size name string
        """
        return self.name


class Product(models.Model):
    """
    Class for product model
    This model contains all the products
    """
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

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
    size = models.ManyToManyField(
        Size,
        max_length=254,
        through='Inventory',
        null=True,
        blank=True,
        related_name='products'
    )

    is_active = models.BooleanField(
        default=False
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    slug = models.SlugField(
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Returns the Product name string
        Args:
            self (object): self.
        Returns:
            The Product name string
        """
        return self.name

    def get_categories(self):
        """
        Returns the product categories list
        Args:
            self (object): self.
        Returns:
            product categories list
        """
        return "\n".join([cat.name for cat in self.category.all()])
    get_categories.short_description = "Categories"

    def get_product_size(self):
        """
        Returns the product size list
        Args:
            self (object): self.
        Returns:
            product size list
        """
        return "\n".join([size.name for size in self.size.all()])
    get_product_size.short_description = "size"

    def save(self, *args, **kwargs):
        """
        Override the save function to update slug value
        """
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Inventory(models.Model):
    """
    Class for inventory model
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='inventories',
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        null=True,
        blank=True
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
        Returns a random unique sku string
        Args:
            self (object): self.
        Returns:
            The sku string
        """
        unique = True
        while unique:
            sku_ref = 'pp'+str(random.randint(1010201, 1011031))
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
        Returns the product sku string
        Args:
            self (object): self.
        Returns:
            The product sku string
        """
        return self.sku
