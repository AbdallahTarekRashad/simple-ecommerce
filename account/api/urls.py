from django.urls import path, re_path
from rest_framework import permissions

from .views import UserRegisterView, UserLoginAPIView, Me
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
app_name = 'accounts_api'
urlpatterns = [
    path('api/signup/', UserRegisterView.as_view(), name='api_signup'),
    path('api/login/', UserLoginAPIView.as_view(), name='api_login'),
    path('api/me/', Me.as_view(), name='api_me'),
]
