from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        TEACHER = 'TE', 'Teacher/Mentor'
        STUDENT = 'ST', 'Student'
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=125)
    role = models.CharField(max_length=2, choices=Role.choices)
    phone_number = PhoneNumberField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'role']


    objects = CustomUserManager()

    def __str__(self):
        return self.email