from django.urls import path

from order.views import OrderAPIView

urlpatterns = [

    # path('cart1/', cart),
    path('order/', OrderAPIView.as_view()),

]
