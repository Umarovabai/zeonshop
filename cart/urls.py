from django.urls import path

from cart.views import APICartCreateView, APICartDeleteALLView, CartView, DeleteOneCartView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/create/', APICartCreateView.as_view()),
    path('cart/delete/', APICartDeleteALLView.as_view()),
    path('cart/one_delete/', DeleteOneCartView.as_view())
]
