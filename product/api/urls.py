from django.urls import path
from rest_framework.routers import DefaultRouter

from account.api.views import WishView
from product.api.views import SearchView, ProductView, ProductModelViewSet

router = DefaultRouter()

router.register('api/product/search', SearchView, basename='api_search')
router.register('api/product', ProductView, basename='api_product')

router.register('api/admin/products', ProductModelViewSet, basename='api_admin_product')

app_name = 'products_api'
urlpatterns = router.urls

urlpatterns += [
    path('api/wish/', WishView.as_view(), name='wish_view'),
]
