from datetime import date, time, timedelta
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from booking.models import Booking
from users.models import User


class BookingViewsTestCase(TestCase):

    def setUp(self):
        self.managers_group = Group.objects.create(name="Managers")

        # Гость
        self.user_guest = User.objects.create(
            email="guest@example.com",
            password="password123",
            name="Обычный Гость"
        )

        # Менеджер
        self.user_manager = User.objects.create(
            email="manager@example.com",
            password="password123",
            name="Иван Менеджер"
        )
        self.user_manager.groups.add(self.managers_group)

        # Бронь
        self.tomorrow = date.today() + timedelta(days=1)
        self.booking = Booking.objects.create(
            name="Тестовый Клиент",
            phone_number="89990000000",
            count_of_guests=2,
            date=self.tomorrow,
            time=time(19, 0),
            confirmation=False
        )

        # URL
        self.create_url = reverse("booking:booking_create")
        self.list_url = reverse("booking:booking_list")
        self.delete_url = reverse("booking:booking_delete", kwargs={"pk": self.booking.pk})
        self.update_url = reverse("booking:booking_update", kwargs={"pk": self.booking.pk})

    def test_booking_page(self):
        """Создания брони всеми желающими"""
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_booking_create(self):
        """Создание брони"""
        data = {
            "name": "Новый Гость",
            "phone_number": "89991112233",
            "count_of_guests": 4,
            "date": self.tomorrow,
            "time": time(20, 0),
            "confirmation": False
        }
        response = self.client.post(self.create_url, data=data)

        self.assertRedirects(response, reverse("booking:confirmation"))

    def test_booking_list_for_user(self):
        """Обычному пользователю закрыт доступ к списку бронирований"""
        self.client.force_login(self.user_guest)
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 403)

    def test_booking_list_for_manager(self):
        """Менеджер имеет доступ к списку бронирований"""
        self.client.force_login(self.user_manager)
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)

    def test_booking_update_for_user(self):
        """Обычный пользователь не может редактировать бронирования"""
        self.client.force_login(self.user_guest)
        response = self.client.get(self.update_url)

        self.assertEqual(response.status_code, 403)

    def test_booking_update_for_manager(self):
        """Менеджер может подтвердить бронь"""
        self.client.force_login(self.user_manager)
        data = {
            "name": self.booking.name,
            "phone_number": self.booking.phone_number,
            "count_of_guests": self.booking.count_of_guests,
            "date": self.booking.date,
            "time": self.booking.time,
            "confirmation": True
        }
        self.client.post(self.update_url, data=data)

        self.booking.refresh_from_db()
        self.assertEqual(self.booking.confirmation, True)

    def test_booking_delete_for_user(self):
        """Обычный пользователь не может удалить бронирование"""
        self.client.force_login(self.user_guest)
        response = self.client.post(self.delete_url)

        self.assertEqual(response.status_code, 403)

    def test_booking_delete_for_manager(self):
        """Менеджер может удалить бронирование."""
        self.client.force_login(self.user_manager)
        self.client.post(self.delete_url)

        self.assertFalse(Booking.objects.filter(pk=self.booking.pk).exists())
