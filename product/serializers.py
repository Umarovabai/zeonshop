from rest_framework import serializers

from product.models import Product, Category, ProductItemImage, AboutUs, Help, \
    OurAdvantages, PublicOffer, Help_image, News, Slider, Footer, \
    FloatingButton, Contacts


class CategorySerializer(serializers.ModelSerializer):
    """ Сериализатор для коллекции """

    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class CategoryGetSerializer(serializers.ModelSerializer):
    """ Сериализатор для получении колекции """
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'image')

    def get_image(self, obj):
        try:
            request = self.context.get('context')
            image = obj.image.path
            print(self.context.get('context'))
            return request.build_absolute_uri(image)
        except AttributeError:
            return None
        except ValueError:
            return None


class ProductItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItemImage
        fields = ('image', 'rgb_color')


class ListProductSerializer(serializers.Serializer):
    """ Список товаров """
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'product_item_image', 'name', 'price', 'old_price', 'discount', 'size_range')


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для товара """
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'artikul', 'price', 'old_price', 'discount',
                  'description', 'composition', 'stock', 'material', 'product_item_image')


class SimilarSerializer(serializers.ModelSerializer):
    """ Похожие товары """
    product_item_image = ProductItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'product_item_image', 'name', 'price', 'old_price', 'discount', 'size_range')


class AboutUsSerializer(serializers.ModelSerializer):
    """ Сериализатр для О нас """

    class Meta:
        model = AboutUs
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    """ Сериализатор для помощи """

    class Meta:
        model = Help
        fields = ['question', 'answer']


class Help_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help_image
        fields = ['image_help']


class OurAdvantagesSerializer(serializers.ModelSerializer):
    """ Сериализатор для наши преимущества """

    class Meta:
        model = OurAdvantages
        fields = ('title', 'description', 'image')


class PublicOfferSerializer(serializers.ModelSerializer):
    """ Сериализатор для публичной офферты """

    class Meta:
        model = PublicOffer
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    """ Сериализатор для новости """

    class Meta:
        model = News
        fields = '__all__'


class NoveltiesListSerializer(serializers.Serializer):
    """ Сериализатор для новинок """

    class Meta:
        model = Product
        fields = ('id', 'image', 'name', 'price', 'old_price', 'discount', 'size_range')


class SliderSerializers(serializers.ModelSerializer):
    """ Сериализатор для слайдера """

    class Meta:
        model = Slider
        fields = ('link', 'image')


class FooterSerializers(serializers.ModelSerializer):
    """ Сериализатор для футер и хедера """

    class Meta:
        model = Footer
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контактных данных """

    class Meta:
        model = Contacts
        fields = ('instagram', 'mail',
                  'whatsapp', 'num', 'telegram')


class FloatingButtonSerializer(serializers.ModelSerializer):
    """ Сериализатор для обратного звонка """

    class Meta:
        model = FloatingButton
        fields = ('whatsapp', 'telegram')
