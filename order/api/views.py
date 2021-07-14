from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from order.api.serializers import OrderSerializer
from order.models import Order
from product.models import Product


class OrderView(CreateModelMixin, GenericViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        product = Product.objects.get(id=request.data['product'])
        order = Order(product=product, customer=request.user, quantity=request.data['quantity'])
        order.save()

        serializer = self.serializer_class(order)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
