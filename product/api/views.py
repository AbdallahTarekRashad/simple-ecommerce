from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from product.api.serializers import ProductSerializer
from product.models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

field_expand = [
    openapi.Parameter('fields', in_=openapi.IN_QUERY,
                      description='A query with the fields parameter on the other hand returns only a subset of the '
                                  'fields',
                      type=openapi.TYPE_STRING),
    openapi.Parameter('omit', in_=openapi.IN_QUERY,
                      description='A query with the omit parameter excludes specified fields',
                      type=openapi.TYPE_STRING)]


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=field_expand))
class SearchView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'price': ['gte', 'lte'],
        'name': ['icontains'],
    }
    search_fields = ['name']
    ordering_fields = ['price']
    ordering = ['id']


class ProductView(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@method_decorator(name='retrieve', decorator=swagger_auto_schema(manual_parameters=field_expand))
@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=field_expand))
@method_decorator(permission_required('products.view_product', raise_exception=True), name='list')
@method_decorator(permission_required('products.view_product', raise_exception=True), name='retrieve')
class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [DjangoObjectPermissions]
    pagination_class = StandardResultsSetPagination
