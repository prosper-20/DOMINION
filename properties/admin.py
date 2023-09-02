from django.contrib import admin
from .models import Property, Appointment

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", 'bedrooms', 'price', 'square_feet', "property_type", "agent"]
    list_filter = ["bedrooms", "status", "bathrooms", "agent"]
    list_editable= ["price"]
    prepopulated_fields = {"slug": ("title",)}



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["property", "name", "phone_number"]
    list_filter = ["name", "property"]
