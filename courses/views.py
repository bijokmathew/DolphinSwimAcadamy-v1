"""
 Module view for Courses app
"""

# Imports

# -----------------------------------------------------------------
# 3rd Party
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
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

    def __init__(self):
        self.no_search_result = True

    def get_queryset(self, **kwargs):
        search_results = CourseFilter(
            self.request.GET, self.queryset
        )
        if search_results.qs:
            self.no_search_result = False
        # Returns the default queryset if an
        # empty queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

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
        context.update({"Error": "Sorry!, Failed to add the course.\
             Please ensure the form is valid"})
        messages.error(self.request, 'Sorry!, Failed to add the course.\
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


class CourseEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A class based view to create template view for
    editing the existing course
    Args:
        request (object): HTTP request object.
    Returns:
        Render of course edit page with context
    """
    model = Course
    form_class = CorseForm
    raise_exception = False
    redirect_field_name = '/'
    login_url = '/accounts/login'
    template_name = 'courses/course_edit.html'
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
        context.update({"Error": "Sorry!, Failed to add the course.\
             Please ensure the form is valid"})
        messages.error(self.request, 'Sorry!, Failed to add the course.\
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
                f"Successfully {course.name} updated to the store"
        )
        return super().form_valid(form)


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A class based view to delete a course
    Args:
        request (object): HTTP request object.
    Returns:
        Deleted course and show alert to the user
    """
    model = Course
    raise_exception = False
    redirect_field_name = '/'
    success_url = reverse_lazy('courses')
    login_url = '/accounts/login'
    template_name = 'courses/course_confirm_delete.html'
    permission_denied_message = "Sorry, You are not autherized to \
        perform this action"

    def test_func(self):
        """
        Override the default behavior to check
        whether the user is admin
        """
        return self.request.user.is_superuser

    def get_object(self, queryset=None):
        """
        A method to get the object
        """
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Course, slug=slug_)

    def delete(self, request, *args, **kwargs):
        """
        Override the delete function to
        show custom message
        """
        messages.success(
                self.request,
                f"Course Deleted!"
        )
        return super().delete(request, *args, **kwargs)
