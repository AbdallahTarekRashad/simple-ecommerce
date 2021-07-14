from rest_flex_fields import FlexFieldsModelSerializer

from product.models import Product


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'inventory']
