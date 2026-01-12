from captcha.fields import CaptchaField
from django import forms
from .models import Course, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class CourseForm(forms.ModelForm):
    captcha = CaptchaField(label="Введіть код з картинки")
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'level', 'duration', 'category','rate', 'image_url']