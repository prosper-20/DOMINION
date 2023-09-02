from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, AgentRegistrationSerializer
from rest_framework.permissions import IsAuthenticated


class UserRegisterView(APIView):
    def post(self, request, format=None):
        new_user = UserRegistrationSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()
        print(new_user)
        message = {"Success": "Account has been created successfully"}
        message.update(new_user.data)
        return Response(message, status=status.HTTP_201_CREATED)



class AgentRegisterView(APIView):
    def post(self, request, format=None):
        new_user = AgentRegistrationSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()
        print(new_user)
        message = {"Success": "Agent account has been created successfully"}
        message.update(new_user.data)
        return Response(message, status=status.HTTP_201_CREATED)
