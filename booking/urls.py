from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from booking.apps import BookingConfig
from booking.views import home_view, BookingCreateView, confirmation_view, menu_view, BookingListView, \
    BookingDeleteView, BookingUpdateView, about_view, contact_view

app_name = BookingConfig.name

urlpatterns = [
    path('', home_view, name="home"),
    path('confirmation/', confirmation_view, name="confirmation"),
    path('menu/', menu_view, name="menu"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),

    path('booking/new/', BookingCreateView.as_view(), name="booking_create"),
    path('booking_list/', BookingListView.as_view(), name="booking_list"),
    path('booking/<int:pk>/edit/', BookingUpdateView.as_view(), name="booking_update"),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name="booking_delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
