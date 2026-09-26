from django.test import TestCase
from django.urls import reverse
from users.models import User


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse("users:register")

        self.user = {
            "email": "test_user@sky.pro",
            "name": "Тестовый Пользователь",
            "password1": "Password12345sa!",
            "password2": "Password12345sa!",
        }

    def test_register_page(self):
        """Страница регистрации доступна неавторизованному пользователю"""
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        """Создание пользователя"""
        response = self.client.post(self.register_url, data=self.user)

        user_exists = User.objects.filter(email="test_user@sky.pro").exists()
        self.assertTrue(user_exists)

        user = User.objects.get(email="test_user@sky.pro")
        self.assertTrue(user.is_active)
