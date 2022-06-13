from rest_framework import serializers

from product.models import Product, Category, ProductItemImage, About_us, Help, OurAdvantages, \
    PublicOffer, ProductItem, Help_image, News, Slider, Footer, FloatingButton


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('size_range', 'quantity_in_line')


class ProductItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItemImage
        fields = ('image', 'rgbcolor')


class ProductSerializer(serializers.ModelSerializer):
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('category', 'name', 'artikul', 'price', 'old_price', 'discount',
                  'description', 'composition', 'stock', 'material', 'product_item_image')


class SimilarSerializer(serializers.ModelSerializer):
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'product_item_image', 'name', 'price', 'old_price', 'discount', 'size_range')


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_us
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['question', 'answer', 'image']


class Help_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help_image
        fields = ['image_help']


class OurAdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAdvantages
        fields = ('title', 'description', 'image')


class PublicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ListProductSerializer(serializers.Serializer):
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'product_item_image', 'name', 'price', 'old_price', 'discount', 'size_range')


class NoveltiesListSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = ('id', 'image', 'name', 'price', 'old_price', 'discount', 'size_range')


class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('link', 'image')


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('info', 'header_image', 'footer_Image',
                  'header_number', 'instagram', 'mail',
                  'whatsapp', 'num', 'telegram')


class FloatingButtonSerlializer(serializers.ModelSerializer):
    class Meta:
        model = FloatingButton
        fields = ('whatsapp', 'telegram')