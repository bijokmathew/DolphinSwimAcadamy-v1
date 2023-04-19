"""
Courses app related models
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# internal
# ------------------------------------------------------------------


class Course(models.Model):
    """
    Course model
    This model describe all the courses related to the swiming
    """
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    class CourseLevels(models.TextChoices):
        BEGINNER = "beginner", "Start to Swim"
        INTERMEDIATE = "intermediate", "Learn to Swim"
        ADVANCED = "advanced", "Confident swimmers"
        LEVEL_1 = "Level-1", "Level-1"
        LEVEL_2 = "Level-2", "Level-2"
        LEVEL_3 = "Level-3", "Level-3"

    name = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        unique=True,
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True,
    )
    description = models.TextField(
        max_length=1256,
        blank=True,
        null=True
    )
    extra_details = models.TextField(
        max_length=1256,
        blank=True,
        null=True
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
    )
    duration_weeks = models.IntegerField(
    )
    level = models.CharField(
        max_length=50,
        choices=CourseLevels.choices,
        default=CourseLevels.BEGINNER
    )
    image = models.ImageField(
        upload_to='courses/',
        blank=True,
        null=True,
        )
    slug = models.SlugField(
        blank=True,
        null=True,
        unique=True,
        )

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        A method to return the absolute url
        """
        return reverse('course_detail', args=[str(self.slug)])

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.name)
