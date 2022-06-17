from rest_framework import serializers

from product.models import Product, Category, ProductItemImage, AboutUs, Help, OurAdvantages, \
    PublicOffer, Help_image, News, Slider, Footer, FloatingButton, Contacts


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class ProductItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItemImage
        fields = ('image', 'rgb_color')


class ProductSerializer(serializers.ModelSerializer):
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'artikul', 'price', 'old_price', 'discount',
                  'description', 'composition', 'stock', 'material', 'product_item_image')


class SimilarSerializer(serializers.ModelSerializer):
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'product_item_image', 'name', 'price', 'old_price', 'discount', 'size_range')


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['question', 'answer']


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

class FooterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('instagram', 'mail',
                  'whatsapp', 'num', 'telegram')


class FloatingButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloatingButton
        fields = ('whatsapp', 'telegram')