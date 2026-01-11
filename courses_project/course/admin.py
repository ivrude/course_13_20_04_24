from django.contrib import admin


from .models import Course, Bucket



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "price",
        "teacher",
    )
    list_editable = ("price", "teacher")
    list_filter = ("price", "teacher")
    ordering = ("id",)

@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "course",
        "count",
        "status",
    )

    list_editable = ("status",)
    ordering = ("id",)

