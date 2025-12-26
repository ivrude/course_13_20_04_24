from django.urls import path
from .views import add_course_view, list_courses_view, add_category_view, list_categories_view, course_detail_view, \
    add_to_busket, bucket_view, delete_bucket

app_name = 'course'

urlpatterns = [
    path('add-course/', add_course_view, name='add_course'),
    path('list/', list_courses_view, name='list_courses'),
    path('add-category/', add_category_view, name='add_category'),
    path('categories/', list_categories_view, name='list_categories'),
    path('list/<int:course_id>/', course_detail_view, name='course_detail'),
    path('list/add_to_busket/<int:course_id>/', add_to_busket, name='add_to_busket'),
    path("bucket/", bucket_view, name="bucket"),
    path("bucket/delete/<int:course_id>/", delete_bucket, name="bucket_delete"),
]