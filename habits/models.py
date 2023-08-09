from django.db import models
from django.utils import timezone

from users.models import User, NULLABLE


class Habit(models.Model):

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Владелец привычек", **NULLABLE)
    place = models.CharField(max_length=150, verbose_name="Место выполнения привычки")
    time = models.TimeField(default=timezone.now, verbose_name="Время выполнения привычки")
    action = models.CharField(max_length=150, null=False, blank=False, verbose_name="Действие привычки")
    is_pleasant = models.BooleanField(default=False, verbose_name="Флаг приятной привычки")
    link_pleasant = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='Периодичность привычки в днях')
    award = models.CharField(max_length=150, verbose_name="Вознаграждение за выполнение привычки", **NULLABLE)
    duration = models.IntegerField(default=120, verbose_name='Время на выполнения привычки')
    is_public = models.BooleanField(default=False, verbose_name='Флаг публикации')

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = 'Привычки'
