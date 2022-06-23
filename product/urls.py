from django.urls import path
from rest_framework import routers

from product.views import ProductRandomView, ProductListView, CategoryListView, AboutUsView, NewsView, HelpView, \
    ContactsView, FooterView, PublicOfferView, OurAdvantagesView, FloatingButtonView, \
    SimilarProductView, NoveltiesView, BestsellerView, MainNoveltiesView, CollectionAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', CollectionAPIView.as_view()),
    path('similar/', SimilarProductView.as_view()),
    path('novelty/', NoveltiesView.as_view()),
    path('bestseller/', BestsellerView.as_view()),
    path('main_novel/', MainNoveltiesView.as_view()),
    path('about/', AboutUsView.as_view()),
    path('news/', NewsView.as_view()),
    path('help/', HelpView.as_view()),
    path('footer/', FooterView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('back_call/', FloatingButtonView.as_view()),
    path('public_offer/', PublicOfferView.as_view()),
    path('our/', OurAdvantagesView.as_view()),
    path('search_random', ProductRandomView.as_view())
]
