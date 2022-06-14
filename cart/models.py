from django.db import models

from order.models import Order
from product.models import Product, ProductItemImage


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product', blank=True, null=True,
                                verbose_name='Продукт')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_product', blank=True, null=True,
                              verbose_name='Заказы')
    price = models.PositiveIntegerField(default=0, blank=True, verbose_name='Цена')
    stock = models.PositiveIntegerField(null=True, blank=True, verbose_name="Количество в линейке")
    image = models.ForeignKey(ProductItemImage, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Картинка товара')

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.product.discount is not None:
            self.price = self.product.price * self.stock
        else:
            self.price = self.product.old_price * self.stock
        super(Cart, self).save()

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Корзины'