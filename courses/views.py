"""
 Module view for Courses app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, DetailView

# internal
from .models import Course
from .filters import CourseFilter
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


class CourseDetailView(DetailView):
    """
    A class based view to show course detail from the
    the course list
    Args:
        request (object): HTTP request object.
    Returns:
        Render of course detail page with context
    """
    model = Course
