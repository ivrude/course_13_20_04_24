from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator
from user.models import CustomUser

# Create your models here.

class Category(models.Model):
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField(validators=[MaxLengthValidator(500)])

    def __str__(self):
        return self.title


class Course(models.Model):
    class Level(models.TextChoices):
        BEGINNER = 'BG', 'Beginner'
        INTERMEDIATE = 'IN', 'Intermediate'
        ADVANCED = 'AD', 'Advanced'
    title = models.CharField(max_length=200)
    description = models.TextField(validators=[MaxLengthValidator(1000)])
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    image_url = models.URLField(default="https://picsum.photos/300/200?blur=5")
    level = models.CharField(max_length=2, choices=Level.choices)
    duration = models.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses')
    rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.title
