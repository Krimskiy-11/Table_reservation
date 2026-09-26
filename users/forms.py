from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'name', 'phone',)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "guest@example.ru"}
        )

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Гость"}
        )

        self.fields["phone"].widget.attrs.update(
            {"class": "form-control", "placeholder": "+7 (999) 000-00-00"}
        )

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "********"}
        )

        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "********"}
        )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            cleaned_digits = phone.replace("+", "").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
            if not cleaned_digits.isdigit():
                raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "guest@example.ru"
        })
    )

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Пароль"}
        )