# Generated by Django 3.2.7 on 2021-11-04 13:04

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(max_length=300, storage=products.models.PublicMediaStorage, upload_to=''),
        ),
    ]
