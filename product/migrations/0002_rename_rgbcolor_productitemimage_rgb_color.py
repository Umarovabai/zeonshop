# Generated by Django 4.0.5 on 2022-06-16 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productitemimage',
            old_name='rgbcolor',
            new_name='rgb_color',
        ),
    ]
