from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course, Bucket
from django.conf import settings

@receiver(post_save, sender=Course)
def course_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Новий курс створено: {instance.title} від {instance.teacher}")

@receiver(post_save, sender=Bucket)
def bucket_add_signal(sender, instance, created, **kwargs):
    if created:
        from_email = settings.EMAIL_HOST_USER
        message = f'Ви додали курс {instance.course.title} в корзину'
        to_email = instance.user.email
        send_mail(
            "Курс додано в корзину",
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )

