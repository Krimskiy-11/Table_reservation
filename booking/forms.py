import datetime

from django import forms

from .models import Booking

class BookingManagerForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["confirmation"]

    def __init__(self, *args, **kwargs):
        super(BookingManagerForm, self).__init__(*args, **kwargs)

        self.fields["confirmation"].label = "Подтвердить бронирование "

        self.fields["confirmation"].widget.attrs.update(
            {"class": "form-check-input",}
        )


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "phone_number", "count_of_guests", "date", "time"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "count_of_guests": forms.NumberInput(attrs={"min": 1, "max": 10}),
            "phone_number": forms.TextInput(attrs={"type": "tel"}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        self.fields["name"].label = "Ваше имя"
        self.fields["phone_number"].label = "Номер телефона"
        self.fields["count_of_guests"].label = "Количество гостей"
        self.fields["date"].label = "Дата визита"
        self.fields["time"].label = "Время визита"

        self.fields["name"].widget.attrs.update(
            {"class": "form-control",}
        )

        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control",}
        )

        self.fields["count_of_guests"].widget.attrs.update(
            {"class": "form-control",}
        )

        self.fields["date"].widget.attrs.update(
            {"class": "form-control", }
        )

        self.fields["time"].widget.attrs.update(
            {"class": "form-control", }
        )

    def clean_date(self):
        date = self.cleaned_data.get('date')
        data_now = datetime.date.today()
        if date < data_now:
            raise forms.ValidationError("Дата не может быть раньше нынешней даты")
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        time_now = datetime.time()
        if time < time_now:
            raise forms.ValidationError("Время не может быть раньше нынешнего времени")
        return time