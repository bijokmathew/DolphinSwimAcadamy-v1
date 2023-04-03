"""
Profiles app related models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


# internal
# ------------------------------------------------------------------


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery address and order history
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    default_phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    default_street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    default_street_address2 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    default_town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    default_county = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    default_country = CountryField(
        blank_label='Country*',
        null=False,
        blank=False
    )

    def __str__(self):
        """
        Override the __str__() to return username
        """
        return self.user.username

    @receiver(post_save, sender=User)
    def create_update_user_profile(sender, instance, created, **kwargs):
        """
        This function create/update the userprofile when User created/ modiled
        """
        if created:
            UserProfile.objects.create(user=instance)
        # Existing user just save the profile
        instance.userprofile.save()
