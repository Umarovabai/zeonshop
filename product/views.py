from random import choice

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from product.models import Product, Category, AboutUs, Help, OurAdvantages, PublicOffer, News, Slider, \
    Footer, FloatingButton, Contacts

from product.serializers import ProductSerializer, SimilarSerializer, CategorySerializer, AboutUsSerializer, \
    HelpSerializer, OurAdvantagesSerializer, PublicOfferSerializer, NewsSerializer, ListProductSerializer, \
    NoveltiesListSerializer, SliderSerializers, ContactsSerializer, FooterSerializers, FloatingButtonSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'bestseller', 'novelties', 'favorites']
    search_fields = ['category__name', 'name']

class ProductRandomView(APIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):
        try:
            category = list(Category.objects.values_list('id', flat=True).order_by('?'))
            queryset = list(choice(self.queryset.filter(category__id=pk)) for pk in category)[:5]
            serializer = self.serializer_class(queryset, many=True, context={'context': request})
            return Response(serializer.data)
        except IndexError:
            queryset = self.queryset.order_by('?')[:5]
            serializer = self.serializer_class(queryset, many=True, context={'context': request})
            return Response(serializer.data)


class SimilarProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SimilarSerializer

    def get_queryset(self, *args, **kwargs):
        request = Product.objects.filter()
        serializer = SimilarSerializer
        return serializer(request, many=True).data


class CategoryAPIViewsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryAPIViewsPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class AboutUsView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class HelpView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


class OurAdvantagesView(generics.ListAPIView):
    queryset = OurAdvantages.objects.all()[0:4]
    serializer_class = OurAdvantagesSerializer


class PublicOfferView(generics.ListAPIView):
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer


class NewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsViewSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100


class ListProductViewSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class ListProductAPIView(APIView):
    def get(self, po):
        movie = Product.objects.filter(category=po)
        serializer = ListProductSerializer
        return Response(serializer(movie, many=True).data)


class NoveltiesView(generics.ListAPIView):
    queryset = Product.objects.filter(id=True)
    serializer_class = NoveltiesListSerializer


# Слайдер для главной страницы

class SliderAPIViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers


class MainAPIViewsPagination(PageNumberPagination):  # Новинка для главной страницы
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MainNoveltiesView(generics.ListAPIView):
    queryset = Category.objects.filter(id=True)[0:4]
    serializer_class = NoveltiesListSerializer
    pagination_class = MainAPIViewsPagination


# Хит продаж список 8шт со статусом 'хит продаж'
class BestsellerAPIViewsPagination(PageNumberPagination):
    """test"""
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BestsellerView(generics.ListAPIView):
    queryset = Product.objects.filter(bestseller=True)[0:8]
    serializer_class = NoveltiesListSerializer
    pagination_class = BestsellerAPIViewsPagination


class CollectionAPIViewsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CollectionAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()[0:4]
    serializer_class = CategorySerializer
    pagination_class = CollectionAPIViewsPagination


# Наши приемущества список 4шт
class OurAdvantagesView(generics.ListAPIView):
    queryset = OurAdvantages.objects.all()[0:4]
    serializer_class = OurAdvantagesSerializer


class FooterView(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializers

class ContactsView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class FloatingButtonView(generics.CreateAPIView):
    queryset = FloatingButton.objects.all()
    serializer_class = FloatingButtonSerializer