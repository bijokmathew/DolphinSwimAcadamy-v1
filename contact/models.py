"""
Contact App related models
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django_countries.fields import CountryField

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Contact(models.Model):
    """
    This model describes the contact details
    """
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    class ContactOption(models.TextChoices):
        """
        Defines the contact options
        """
        PRODUCT = 'Product', 'Product Shopping'
        COURSE = 'Course', 'Course Booking'
        GENERAL = 'General', 'General Queries'

    subject = models.CharField(
        max_length=50,
        choices=ContactOption.choices,
        default=ContactOption.GENERAL
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
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    street_address = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    county = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    country = CountryField(
        blank_label='Country*',
        null=False,
        blank=False
    )
    message = models.TextField(
        max_length=1020
    )

    def __str__(self):
        """
        Override the __str__() to return full name
        """
        return self.full_name
