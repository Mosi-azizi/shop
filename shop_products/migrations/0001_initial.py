# Generated by Django 3.1 on 2021-07-19 03:21

from django.db import migrations, models
import shop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop_products.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]