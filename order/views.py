from rest_framework import generics

from order.models import OrderItem
from order.serializers import OrderSerializer


class OrderAPIView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer