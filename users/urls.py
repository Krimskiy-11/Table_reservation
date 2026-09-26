from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.forms import UserLoginForm
from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name='users/login.html', authentication_form=UserLoginForm), name='login'),
    path("logout/", LogoutView.as_view(next_page="booking:home"), name='logout'),
    path("register/", RegisterView.as_view(), name='register'),
]