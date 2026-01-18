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
    course = serializers.SlugRelatedField(slug_field="description", read_only=True)
    user = serializers.SlugRelatedField(slug_field="email", read_only=True)
    class Meta:
        model = Bucket
        fields = ["id", "count", "status", "user", "course"]