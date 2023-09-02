from django.db import models
from users.models import CustomUser

class Property(models.Model):
    PROPERTY_TYPES = (
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        # Add more property types as needed
    )

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        # Add more status choices as needed
    )

    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True, null=True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveBigIntegerField()
    square_feet = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    list_date = models.DateField(auto_now_add=True)
    photo_main = models.ImageField(upload_to='properties/')
    photo_1 = models.ImageField(upload_to='properties/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='properties/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='properties/', blank=True, null=True)
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title
    


class Appointment(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.property.title
