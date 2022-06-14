from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from product.views import ProductRandomView, ProductListView, CategoryListView, AboutUsView, NewsView, HelpView, \
    ContactsView, FooterView, PublicOfferView, OurAdvantagesView, FloatingButtonView
#
# router = routers.DefaultRouter()
# router.register('novelties', NoveltiesListAPIViewSet)
# router.register('slider', SliderAPIViewSet)
# router.register('bestseller', BestsellerAPIViewSet)
# router.register('similar', SimilarProductAPIViewSet, basename='Similar')

urlpatterns = [
    # path('', include(router.urls)),
    path('products/', ProductListView.as_view(), name='product'),
    path('collections/', CategoryListView.as_view(), name='category'),
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