from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course

@receiver(post_save, sender=Course)
def course_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Новий курс створено: {instance.title} від {instance.teacher}")