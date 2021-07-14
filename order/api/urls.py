from django.urls import path
from rest_framework.routers import DefaultRouter

from order.api.views import OrderView

router = DefaultRouter()

router.register('api/order', OrderView, basename='api_order')
urlpatterns = router.urls

app_name = 'orders_api'

