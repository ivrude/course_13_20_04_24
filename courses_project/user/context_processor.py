from .models import Notification

def notifications_processor(request):
    if request.user.is_authenticated:
        notifications = (
            Notification.objects
            .filter(user=request.user, is_read=False)
            .only("id", "message", "created_at")
        )

        return {
            "global_notifications": notifications[:5],  # показуємо тільки 5
            "notifications_count": notifications.count()
        }

    return {}