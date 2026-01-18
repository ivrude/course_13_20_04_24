from django.urls import path
from .api_views import CourseListAPI, CourseCreateAPI, GoogleLoginView, GoogleCallbackView, BucketListAPI

urlpatterns = [
    path("courses/", CourseListAPI.as_view(), name="api_courses"),
    path("courses/create/", CourseCreateAPI.as_view(), name="api_course_create"),
    path("buckets/", BucketListAPI.as_view(), name="api_buckets"),
    path('auth/google/login/', GoogleLoginView.as_view()),
    path('auth/google/callback/', GoogleCallbackView.as_view()),
]
