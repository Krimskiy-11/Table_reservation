from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "phone_number", "count_of_guests", "date", "time"]

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

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