# Generated by Django 4.0.5 on 2022-06-16 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_remove_orderitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='related_cart', to='basket.order'),
        ),
    ]
