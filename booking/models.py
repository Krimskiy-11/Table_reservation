from django.db import models


class Booking(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Укажите имя гостя"
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Укажите номер телефона"
    )
    count_of_guests = models.PositiveIntegerField(
        default=1,
        verbose_name="Укажите количество гостей"
    )
    date = models.DateField(
        verbose_name="Укажите дату бронирования"
    )
    time = models.TimeField(
        verbose_name="Укажите время бронирования"
    )
    confirmation = models.BooleanField(
        default=False,
        verbose_name="Подтверждение бронирования"
    )

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        permissions = [
            ('can_confirm_booking', 'Can confirm booking')
        ]

    def __str__(self):
        return f"{self.count_of_guests} - {self.name}"
