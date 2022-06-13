from django.urls import path

from cart.views import APICartCreateView

urlpatterns = [
    path('cart/', APICartCreateView.as_view())
]