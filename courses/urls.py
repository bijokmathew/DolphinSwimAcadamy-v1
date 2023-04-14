"""
Courses module url configurations
"""

# ------------------------------------------------
# 3rd party
from django.urls import path

# internal
from . import views
# -------------------------------------------------

urlpatterns = [
    path(
        '',
        views.CourseListView.as_view(),
        name='courses'
    ),
    path(
        'course_detail/<slug:slug>',
        views.CourseDetailView.as_view(),
        name='course_detail'
    ),
]
