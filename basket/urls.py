from django.urls import path

from basket.views import APICartCreateView, APICartDeleteALLView, CartView, DeleteOneCartView, AddOneCartView, \
    OrderAPIView, APICartTotalView, OrderCreateView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/create/', APICartCreateView.as_view()),
    path('cart/del_all/', APICartDeleteALLView.as_view()),
    path('cart/del_one/', DeleteOneCartView.as_view()),
    path('cart/add_one/', AddOneCartView.as_view()),
    path('cart/total/', APICartTotalView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    path('order/', OrderAPIView.as_view()),
]
