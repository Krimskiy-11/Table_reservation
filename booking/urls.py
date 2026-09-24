from django.urls import path
from booking.apps import BookingConfig
from booking.views import home_view, BookingCreateView, confirmation_view, menu_view, BookingListView, \
    BookingDeleteView, BookingUpdateView

app_name = BookingConfig.name

urlpatterns = [
    path('', home_view, name="home"),
    path('confirmation/', confirmation_view, name="confirmation"),
    path('menu/', menu_view, name="menu"),

    path('booking/new/', BookingCreateView.as_view(), name="booking_create"),
    path('booking_list/', BookingListView.as_view(), name="booking_list"),
    path('booking/<int:pk>/edit/', BookingUpdateView.as_view(), name="booking_update"),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name="booking_delete")
]
