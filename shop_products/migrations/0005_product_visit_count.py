# Generated by Django 3.1 on 2021-08-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0004_productgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visit_count',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]
