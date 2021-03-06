# Generated by Django 4.0.5 on 2022-06-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_remove_order_discount_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_amount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Сумма скидки'),
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_goods',
            field=models.IntegerField(default=0, verbose_name='Количество всех товаров в линейках'),
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_lines',
            field=models.IntegerField(default=0, verbose_name='Количество линеек'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_discounted_price',
            field=models.IntegerField(default=0, verbose_name='Сумма всех скидок'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price_before_discount',
            field=models.IntegerField(default=0, verbose_name='Общая цена до учета скидок'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
