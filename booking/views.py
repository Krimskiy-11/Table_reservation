from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from booking.forms import BookingForm
from booking.models import Booking


def home_view(request):
    return render(request, 'booking/base.html')


def confirmation_view(request):
    return render(request, 'booking/confirmation.html')


def menu_view(request):
    return render(request, 'booking/menu.html')


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy("booking:confirmation")

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "booking/booking_list.html"

    # def get_queryset(self):
    #     if self.request.user.groups.filter(name='Managers').exists():
    #         qs = Booking.objects.all()
    #     else:
    #         qs = Booking.objects.filter(owner=self.request.user)
    #     return qs


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    success_url = reverse_lazy("booking:booking_list")


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking:booking_list")
