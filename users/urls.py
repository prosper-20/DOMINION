from django.urls import path, include
from .views import UserRegisterView, AgentRegisterView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("signup/", UserRegisterView.as_view(), name="user-signup"),
    path('auth/', include('djoser.urls.authtoken')),
    path("signup/agent/", AgentRegisterView.as_view(), name="agent-signup")
]