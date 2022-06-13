from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from product.views import Help, OurAdvantagesAPIViewSet, FooterAPIViewSet, ProductViewSet, \
    CategoryListAPIViewSet, AboutUsAPIViewSet, PublicOfferAPIViewSet, NewsViewSet, NoveltiesListAPIViewSet, \
    SliderAPIViewSet, BestsellerAPIViewSet, CollectionAPIViewSet, FloatingButtonAPIViewSet, HelpAPIViewSet, \
    SimilarProductAPIViewSet, ProductRandomView

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('Our', OurAdvantagesAPIViewSet)
router.register('footer', FooterAPIViewSet)
router.register('categories', CategoryListAPIViewSet)
router.register('about_as', AboutUsAPIViewSet)
router.register('public_offer', PublicOfferAPIViewSet)
router.register('news', NewsViewSet)
router.register('novelties', NoveltiesListAPIViewSet)
router.register('slider', SliderAPIViewSet)
router.register('bestseller', BestsellerAPIViewSet)
router.register('category', CollectionAPIViewSet)
router.register('back_call', FloatingButtonAPIViewSet)
router.register('help', HelpAPIViewSet)
router.register('similar', SimilarProductAPIViewSet, basename='Similar')

urlpatterns = [
    path('', include(router.urls)),
    path('search_random', ProductRandomView.as_view())
]