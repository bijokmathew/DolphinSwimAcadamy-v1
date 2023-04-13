"""
 Module view for Courses app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView

# internal
from .models import Course
# ------------------------------------------------------------------


class CourseListView(ListView):
    """
    Class based view for listing all swim courses
    """
    model = Course

    def get_queryset(self, **kwargs):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(
            self.request.GET, queryset=self.get_queryset()
        )
        return context
