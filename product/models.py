from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from colorfield.fields import ColorField

STATUS_CALLED = [
    ('YES', 'Да'),
    ('NO', 'Нет')
]

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='products', verbose_name="Картинка")

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Категории')
    name = models.CharField(max_length=150, verbose_name='Название')
    artikul = models.CharField(max_length=200, verbose_name='Артикул')
    price = models.IntegerField(default=True, null=True, blank=True, verbose_name='Цена')
    old_price = models.IntegerField(default=True, verbose_name='Старая цена')
    discount = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Скидки')
    description = RichTextField(verbose_name='Описание')
    size_range = models.CharField(max_length=100, verbose_name='Размерный ряд')
    composition = models.CharField(max_length=100, verbose_name='Состав ткани')
    stock = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name='Количество в линейке')
    material = models.CharField(max_length=100, verbose_name='Материал')
    bestseller = models.BooleanField(default=True, verbose_name='Хит продаж')
    novelties = models.BooleanField(default=True, verbose_name='Новинки')
    favorites = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        dis = self.old_price * self.discount / 100
        self.price = self.old_price - dis
        self.stock = (int(self.size_range[3:]) - int(self.size_range[0:2]) + 2) // 2
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    size_range = models.CharField(max_length=100, null=True, blank=True, verbose_name='Размерный ряд')
    quantity_in_line = models.IntegerField(null=True, blank=True, verbose_name='Количество в линейке')
    Product_item = models.ForeignKey(Product, related_name='product_size', on_delete=models.CASCADE)


def validate_even(value):
    if value == 2:
        raise ValidationError(("%(value)s is not an even number"), params={'value': value})


class ProductItemImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item_image')
    image = models.ImageField(upload_to='products', null=True, blank=True, validators=[validate_even])
    rgbcolor = ColorField(verbose_name='Выбор цветов')

    class Meta:
        verbose_name_plural = 'Картинка продукта'


class About_us(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = RichTextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинки')

    class Meta:
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title





class Help(models.Model):
    question = models.TextField(max_length=200, db_index=True, verbose_name='Вопросы')
    answer = models.TextField(max_length=200, db_index=True, verbose_name='Ответы')
    image = models.ImageField(upload_to='products', verbose_name='Картинки')

    class Meta:
        verbose_name_plural = 'Помощь'

    def __str__(self):
        return self.question


class Help_image(models.Model):
    image_help = models.ImageField(upload_to='products', blank=True, verbose_name='Картинки')

    def clean(self):
        Help.append(len(Help_image.objects.filter(image_help=self.pk)))
        dd = len(Help_image)
        print(len(Help_image))
        if dd >= 2:
            Help.clear()
            raise ValidationError('Не больше 1 Фотографий')


class OurAdvantages(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Наши преимущества'

    def __str__(self):
        return self.title


class PublicOffer(models.Model):
    name = models.CharField(max_length=300, verbose_name='Заголовок')
    description = RichTextField(null=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Публичная офферта'

    def __str__(self):
        return self.name


class News(models.Model):
    image_news = models.ImageField(upload_to='products', blank=True, verbose_name='Картинка')
    header = models.CharField(max_length=200, blank=True, verbose_name='Заголовок')
    description = RichTextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.header


class Slider(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name='Картинка')
    link = models.URLField(max_length=150, null=True, blank=True, verbose_name='Ссылка')

    class Meta:
        verbose_name_plural = 'Слайдер'


class Footer(models.Model):
    info = models.TextField(max_length=200, verbose_name='Информация')
    header_image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Логотип Футера')
    footer_Image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name='Логотип Хедера')
    header_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер в хедере')
    number = models.CharField(max_length=30, blank=True, verbose_name='Ввод данных')
    instagram = models.CharField(max_length=100, null=True, blank=True, verbose_name='Инстаграм')
    whatsapp = models.CharField(max_length=30, null=True, blank=True, verbose_name='Ватсапп')
    telegram = models.CharField(max_length=30, null=True, blank=True, verbose_name='Телеграм')
    mail = models.CharField(max_length=50, null=True, blank=True, verbose_name='Почта')
    num = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер')

    def save(self, *args, **kwargs):
        self.whatsapp = 'https://wa.me/' + self.whatsapp
        self.telegram = 'https://t.me/'
        self.instagram = 'https://www.instagram.com/'
        self.mail = 'https://mail.doodle.com/'
        self.number = '+996{self.number}'
        super(Footer, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Футер и Хедер'


class FloatingButton(models.Model):
    whatsapp = models.CharField(max_length=30, null=True, blank=True, editable=False, verbose_name='Ватсапп')
    telegram = models.CharField(max_length=30, null=True, blank=True, editable=False, verbose_name='Телеграм')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    type = models.CharField(max_length=30, choices=STATUS_CALLED, default='NO', null=True, blank=True, verbose_name='Тип обращения(обратный звонок)')
    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def save(self, *args, **kwargs):
        self.whatsapp = f'https://wa.me/{self.whatsapp}/'
        self.telegram = f'https://t.me/{self.telegram}/'

        super(FloatingButton, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Обратный звонок'