from django.core.cache import cache
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course, Bucket, EmailLog
from django.conf import settings


from user.models import CustomUser, Notification


@receiver(post_save, sender=Course)
def invalidate_courses_cache(sender, **kwargs):
    cache.delete("courses_list")

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
        EmailLog.objects.create(
            subject="Курс додано в корзину",
            to_email=to_email,
        )
@receiver(post_save, sender=CustomUser)
def user_updated_notification(sender, instance, created, **kwargs):
    if not created:  # тільки при оновленні
        Notification.objects.create(
            user=instance,
            message="Ваші дані були оновлені ✅"
        )
