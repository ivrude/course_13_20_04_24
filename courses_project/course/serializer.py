from rest_framework import serializers
from .models import Course, Bucket


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "category",
            "price",
            "duration",
            "level",
            "rate",
            "teacher",
        ]

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        user = serializers.CharField(source="user.full_name", read_only=True)
        fields = ["id", "course", "count", "status", "user"]