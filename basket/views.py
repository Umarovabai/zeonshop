from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from basket.models import Cart, Order, Orders
from basket.serializers import OrderListSerializer, CartCreateSerializer, CartListSerializer, OrderSerializer


class CartView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer


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
    ser_class = CartListSerializer
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
    ser_class = CartListSerializer
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


class APICartTotalView(APIView):
    def get(self, request, *args, **kwargs):
        before_discount = Cart.total_price_before_discount()
        after_discount = Cart.total_price_after_discount()
        discount = before_discount - after_discount
        products = Cart.quantity_all_goods()
        amount = Cart.total_number_of_line()

        return Response({'Сумма до скидки': before_discount,
                         'Сумма после скидки': after_discount,
                         'Скидка': discount,
                         'Количество всех товаров в линейке': products,
                         'Количество всех линеек': amount})


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        order = serializer.save()
        for a in Cart.objects.all():
            Orders.objects.create(product=a.product, name=a.product.name, image=a.image, order=order)
        self.queryset.update()
        Cart.objects.all().delete()


class OrderAPIView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderListSerializer
