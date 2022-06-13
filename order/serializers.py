from rest_framework import serializers

from product.models import ProductItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('__all__')