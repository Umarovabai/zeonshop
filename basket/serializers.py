
from rest_framework import serializers

from basket.models import Cart, OrderItem
from product.models import Product, ProductItemImage


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ('price', )


class ItemCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'size_range', 'price', 'old_price', 'stock']


class ImageCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductItemImage
        fields = ['image', 'rgb_color']


class CartSerializer(serializers.ModelSerializer):
    product = ItemCartSerializer()
    image = ImageCartSerializer()

    class Meta:
        model = Cart
        fields = ['stock', 'price', 'product', 'image']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'




