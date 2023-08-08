from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name="Имя пользователя(как в TG)")
    tg_user_id = models.IntegerField(verbose_name="ID в телеграме", **NULLABLE)
    # email = models.EmailField(unique=True, verbose_name='Почта', **NULLABLE)
    # register_uuid = models.CharField(max_length=50, **NULLABLE)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
