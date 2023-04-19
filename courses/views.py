"""
 Module view for Courses app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.shortcuts import render, get_object_or_404, reverse, redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages

# internal
from .models import Course
from .forms import CorseForm
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


class CourseAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A class based view to create template view for
    adding the course to the model
    Args:
        request (object): HTTP request object.
    Returns:
        Render of course add page with context
    """
    model = Course
    form_class = CorseForm
    raise_exception = False
    redirect_field_name = '/'
    login_url = '/accounts/login'
    template_name = 'courses/course_add.html'
    permission_denied_message = "Sorry, You are not autherized to \
        perform this action"

    def test_func(self):
        """
        Override the default behavior to check
        whether the user is admin
        """
        return self.request.user.is_superuser

    def form_invalid(self, form):
        """
        Override the form_invalid function to
        show custom message
        """
        context = self.get_context_data(form=form)
        context.update({"Error": "Sorry!, Failed to add the product.\
             Please ensure the form is valid"})
        messages.error(self.request, 'Sorry!, Failed to add the product.\
             Please ensure the form is valid')
        return self.render_to_response(context)

    def form_valid(self, form):
        """
        Override the form_valid function to
        show custom message
        """
        course = form.save()
        messages.success(
                self.request,
                f"Successfully {course.name} added to the store"
        )
        return super().form_valid(form)