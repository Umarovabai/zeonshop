from django.urls import path

from basket.views import APICartCreateView, APICartDeleteALLView, CartView, DeleteOneCartView, AddOneCartView, \
    OrderAPIView

urlpatterns = [
    path('basket/', CartView.as_view()),
    path('basket/create/', APICartCreateView.as_view()),
    path('basket/del_all/', APICartDeleteALLView.as_view()),
    path('basket/del_one/', DeleteOneCartView.as_view()),
    path('basket/add_one/', AddOneCartView.as_view()),
    path('order/', OrderAPIView.as_view()),
]
