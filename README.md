



celery -A config worker -l DEBUG
celery -A config beat -l DEBUG --scheduler django_celery_beat.schedulers:DatabaseScheduler