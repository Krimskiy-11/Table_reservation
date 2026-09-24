from django.db import models

class Table(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название стола"
    )
    count_of_seats = models.PositiveIntegerField(
        verbose_name="Количество посадочных мест"
    )
    is_reservation = models.BooleanField(
        default=False,
        verbose_name="Статус бронирования"
    )

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return f"{self.name}"


