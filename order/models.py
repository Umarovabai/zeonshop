from django.db import models

from product.models import Product

Status = (
    ('Оформлен', 'Оформлен'),
    ('Отменен', 'Отменен'),
    ('Новый', 'Новый'),

)


class Order(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя')
    lastname = models.CharField(max_length=100, null=True, blank=True, verbose_name='Фамилия')
    mail = models.CharField(max_length=50, null=True, blank=True, verbose_name='Почта')
    num = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер')
    country = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='Город')
    date_order = models.CharField(max_length=30, null=True, blank=True, verbose_name='Дата оформления')
    status = models.CharField(choices=Status,
                              max_length=255,
                              db_index=True,
                              default=('Новый', 'Новый'), verbose_name='Выбор из списка')
    class Meta:
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.name)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='related_cart', blank=True)

    price = models.IntegerField(null=True, blank=True, default=0, verbose_name='Общая цена до учета скидок')
    quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    sum = models.IntegerField(null=True, blank=True, default=0, verbose_name='Количество линеек')
    sum_quantity = models.IntegerField(null=True, blank=True, default=0, verbose_name='Количество всех товаров в '
                                                                                      'линейках')
    discounts = models.IntegerField(null=True, blank=True, default=0, verbose_name='Сумма всех скидок')
    total = models.IntegerField(null=True, blank=True, default=0, verbose_name='Итого к оплате')
    user = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='user', blank=True)

    def save(self, *args, **kwargs):
        if self.id:
            self.quantity = sum([product.quantity for product in self.cart.all()])
            self.sum_quantity = sum([k.quan_sum for k in self.cart.all()])
            self.price = sum([k.price_q for k in self.cart.all()])
            self.discounts = sum([k.rebate for k in self.cart.all()])
            self.total = sum([k.sum_r for k in self.cart.all()])
            self.sum = len(self.cart.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

