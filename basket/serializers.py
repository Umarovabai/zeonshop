
from rest_framework import serializers

from basket.models import Cart, Order
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


class CartListSerializer(serializers.ModelSerializer):
    product = ItemCartSerializer()
    image = ImageCartSerializer()

    class Meta:
        model = Cart
        fields = ['stock', 'price', 'product', 'image']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('status',)
        read_only_fields = ('id',
                            'number_of_lines',
                            'number_of_goods',
                            'total_price_before_discount',
                            'total_discounted_price',
                            'discount_amount'
                            )

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'




