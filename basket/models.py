from django.db import models
from product.models import Product, ProductItemImage

Status = (
    ('Оформлен', 'Оформлен'),
    ('Отменен', 'Отменен'),
    ('Новый', 'Новый'),

)


class Order(models.Model):
    """ Информация юзера и заказа """
    name = models.CharField(max_length=100, null=True, verbose_name='Имя')
    lastname = models.CharField(max_length=100, null=True, verbose_name='Фамилия')
    mail = models.CharField(max_length=50, null=True, verbose_name='Почта')
    num = models.CharField(max_length=30, null=True, verbose_name='Номер')
    country = models.CharField(max_length=30, null=True, verbose_name='Страна')
    city = models.CharField(max_length=30, null=True, verbose_name='Город')
    date_order = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата оформления')
    status = models.CharField(choices=Status,
                              max_length=255,
                              db_index=True,
                              default=('Новый', 'Новый'), verbose_name='Статус заказа')
    number_of_goods = models.IntegerField(default=0, verbose_name='Количество линеек')
    number_of_lines = models.IntegerField(default=0, verbose_name='Количество всех товаров в линейках')
    total_price_before_discount = models.IntegerField(default=0, verbose_name='Общая цена до учета скидок')
    total_discounted_price = models.IntegerField(default=0, verbose_name='Сумма после скидки')
    discount_amount = models.IntegerField(null=True, blank=True, default=0, verbose_name='Сумма скидки')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.number_of_goods = Cart.quantity_all_goods()
        self.number_of_lines = Cart.total_number_of_line()
        self.total_price_before_discount = Cart.total_price_before_discount()
        self.total_discounted_price = Cart.total_price_after_discount()
        self.discount_amount = self.total_price_before_discount - self.total_discounted_price
        super(Order, self).save()

    class Meta:
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name


class Orders(models.Model):
    """ Заказзанные товары """
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(verbose_name='Название', max_length=200)
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='order')
    image = models.ForeignKey(ProductItemImage, verbose_name='Фото', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заказанные товары'


class Cart(models.Model):
    """ Создание корзины """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product', blank=True, null=True,
                                verbose_name='Продукт')
    amount_products = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество товаров')
    price = models.PositiveIntegerField(default=0, blank=True, verbose_name='Цена')
    stock = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="Количество в линейке")
    image = models.ForeignKey(ProductItemImage, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Картинка товара')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.product.discount:
            self.price = self.product.price * self.stock
        else:
            self.price = self.product.old_price * self.stock
        self.amount_products = self.stock * self.product.stock
        super(Cart, self).save()

    @staticmethod
    def total_price_before_discount():
        """ Общяя стоимость до скидки """
        total = 0
        for orders in Cart.objects.all():
            total += orders.product.old_price * orders.stock
        return total

    @staticmethod
    def total_price_after_discount():
        """ Общяя стоимсть после скидки """
        total = 0
        for orders in Cart.objects.all():
            total += orders.product.price * orders.stock
        return total

    @staticmethod
    def quantity_all_goods():
        """ Количество всех товаров """
        total = 0
        for orders in Cart.objects.all():
            total += orders.amount_products
        return total

    @staticmethod
    def total_number_of_line():
        """ Общяя количество линейки """
        total = 0
        for orders in Cart.objects.all():
            total += orders.stock
        return total

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Корзинa'
