# Generated by Django 3.2.7 on 2021-10-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0002_auto_20211030_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrating',
            name='product_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userproductview',
            name='product_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
