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
        total = product.price * request.data['quantity']
        if product.inventory < request.data['quantity']:
            raise ValidationError({
                'product': "Out Of Stock"
            })
        if total <= 10000:
            product.inventory = product.inventory - request.data['quantity']
            product.save()
            instance = Order.objects.create(customer=request.user, product=product, quantity=request.data['quantity'],
                                            total=total)
        else:
            raise ValidationError({
                'total_of_order': "bigger than 10000.0"
            })

        serializer = self.serializer_class(instance)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
