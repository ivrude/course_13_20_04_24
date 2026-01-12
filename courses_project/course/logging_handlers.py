import logging


class DBLogHandler(logging.Handler):
    def emit(self, record):
        from .models import SystemLog
        SystemLog.objects.create(
            level=record.levelname,
            message=record.getMessage(),
        )