# Generated by Django 3.2.7 on 2022-09-26 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0005_alter_productrating_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProductViewGroupBy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('recsys.userproductview',),
        ),
    ]
