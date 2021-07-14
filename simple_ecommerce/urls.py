from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.api.urls', namespace='account')),
    path('', include('product.api.urls', namespace='product')),
    path('', include('order.api.urls', namespace='order')),

    # Api Documentation

    path('api/doc/swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='api_swagger'),
    path('api/doc/redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='api_redoc'),

    re_path(r'^api/doc/schema(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='api_json_yaml'),
]
