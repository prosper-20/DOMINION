from django.contrib import admin
from .models import CustomUser, Profile

admin.site.register(Profile)


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ["email"]



