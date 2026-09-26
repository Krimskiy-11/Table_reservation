from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from booking.forms import BookingForm, BookingManagerForm
from booking.models import Booking


def home_view(request):
    return render(request, 'booking/base.html')


def confirmation_view(request):
    return render(request, 'booking/confirmation.html')


def menu_view(request):
    return render(request, 'booking/menu.html')


def about_view(request):
    return render(request, 'booking/about.html')


def contact_view(request):
    return render(request, 'booking/contact.html')


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy("booking:confirmation")


class BookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = "booking/booking_list.html"
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Managers").exists()


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    success_url = reverse_lazy("booking:booking_list")
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Managers").exists()


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingManagerForm
    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking:booking_list")
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Managers").exists()
