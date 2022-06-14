from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer

class CartView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

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
        order = serializer.validated_data['order']
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
            # return Response({'stock': order_item.stock}, status=200)



# class DeleteOneAmountBasketView(APIView):
#     """method for delete amount in basket by one"""
#     serializer_class = BasketSerializer
#     model = ItemCart
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'context': request})
#         serializer.is_valid(raise_exception=True)
#         item = serializer.validated_data['item']
#         image = serializer.validated_data['image']
#         if ItemCart.objects.filter(item=item, image=image).exists():
#             orderitem = ItemCart.objects.filter(item=item, image=image).first()
#             orderitem.amount -= 1
#             orderitem.save()
#             if orderitem.amount <= 1:
#                 orderitem.delete()
#                 return Response({'amount': orderitem.amount}, status=204)
#
#         else:
#             return Response({'amount': 0}, status=200)
#         return Response({'amount': orderitem.amount}, status=200)
