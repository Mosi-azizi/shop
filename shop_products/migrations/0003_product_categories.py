# Generated by Django 3.1 on 2021-07-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products_category', '0001_initial'),
        ('shop_products', '0002_auto_20210728_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='shop_products_category.ProductCategory', verbose_name='دسته بندی ها'),
        ),
    ]
