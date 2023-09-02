from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Property, Appointment
from .serializers import PropertySerializer, PropertyDetailSerializer, PropertyAppointmentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAgentCanCreateProperty
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PropertyHomePage(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAgentCanCreateProperty]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticatedOrReadOnly()]
        elif self.request.method == 'POST':
            return [IsAuthenticatedOrReadOnly(), IsAgentCanCreateProperty()]
        return super().get_permissions()

   

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(agent=user)


class PropertyDetailPage(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAgentCanCreateProperty]
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticatedOrReadOnly()]
        elif self.request.method == 'PUT':
            return [IsAuthenticatedOrReadOnly(), IsAgentCanCreateProperty()]
        return super().get_permissions()


class PropertyAppointmentPage(APIView):
    def post(self, request, slug, format=None):
        print(slug)
        property = get_object_or_404(Property, slug=slug)
        print(property)
        serializer = PropertyAppointmentSerializer(property, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        new_appointment = Appointment.objects.create(property=property, name=serializer.data["name"], phone_number=serializer.data["phone_number"])
        message = {"Success": "Your appointment has been made"}
        return Response(message, status=status.HTTP_201_CREATED)

        
