from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from basket.models import Cart, OrderItem
from basket.serializers import OrderSerializer, CartCreateSerializer, CartSerializer


class CartView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class APICartCreateView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'context': request})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class APICartDeleteALLView(APIView):

    def delete(self, *args, **kwargs):
        Cart.objects.all().delete()
        return Response()

class DeleteOneCartView(APIView):
    ser_class = CartSerializer
    model = Cart

    def post(self, request):
        serializer = self.ser_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data['product']
        order = serializer.validated_data['orders']
        image = serializer.validated_data['image']
        if Cart.objects.filter(product=product, order=order, image=image).exists():
            order_item = Cart.objects.filter(product=product, order=order, image=image).first()
            order_item.stock -= 1
            order_item.save()
            if order_item.stock <= 1:
                order_item.delete()
                return Response({'stock': order_item.stock})
        else:
            return Response({'stock': 0})
        return Response({'stock': order_item.stock}, status=200)

class AddOneCartView(APIView):

    ser_class = CartSerializer
    model = Cart
    def post(self, request):
        serializer = self.ser_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data['product']
        order = serializer.validated_data['orders']
        image = serializer.validated_data['image']
        if Cart.objects.filter(product=product, image=image, order=order).exists():
            order_item = Cart.objects.filter(product=product, image=image, order=order).first()
            order_item.stock += 1
            order_item.save()

        else:
            order_item = Cart.objects.create(
                product=product,
                image=image,
                order=order,
                stock=1,
            )
            return Response({'stock': order_item.stock})
        return Response({'stock': order_item.stock})



class OrderAPIView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer




def total():
    total = 0
    for i in OrderItem.objects.all():
        total += i.product.price
        return total

