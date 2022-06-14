from rest_framework import serializers

from order.models import OrderItem
from product.models import ProductItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

