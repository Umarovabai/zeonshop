from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers import CartSerializer


class APICartCreateView(CreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'context': request})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

