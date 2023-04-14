# Imports
# -----------------------------------------------------------------
# 3rd Party
from django.contrib import admin
# internal
from .models import Course
# ------------------------------------------------------------------

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Admin class for Course model
    """
    list_display = ('name',)
