from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity', 'total']
        read_only_fields = ('customer', 'total')
