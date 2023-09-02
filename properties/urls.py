from django.urls import path
from .views import PropertyHomePage, PropertyDetailPage, PropertyAppointmentPage


urlpatterns = [
    path("all/", PropertyHomePage.as_view(), name="properties"),
    path("<slug:slug>/", PropertyDetailPage.as_view(), name="property-detail"),
    path("<slug:slug>/book/appointment/", PropertyAppointmentPage.as_view(), name="appointment")
]