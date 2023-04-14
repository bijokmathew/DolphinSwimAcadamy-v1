"""
Filter module for Courses app
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
import django_filters
# internal
from .models import Course
# ------------------------------------------------------------------


class CourseFilter(django_filters.FilterSet):
    """
    CourseFilter override the django-filterset to
    filter the coures
    """
    class Meta:
        model = Course
        fields = {
            'level': ['iexact'],
        }
