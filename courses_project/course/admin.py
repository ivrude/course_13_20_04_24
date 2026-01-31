#File whith admin model registration


from django.contrib import admin


from .models import Course, Bucket, SystemLog, EmailLog


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

@admin.register(SystemLog)
class SystemLogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "level", "message")
    list_filter = ("level", "created_at")
    search_fields = ("message",)
    ordering = ("-created_at",)

    readonly_fields = ("created_at", "level", "message")


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "to_email",
        "subject",
    )
    list_filter = ("to_email",)
    readonly_fields = (
        "to_email",
        "subject",
    )
