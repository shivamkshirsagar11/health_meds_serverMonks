# Generated by Django 2.2.1 on 2022-07-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_cart_generator_cart_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_item',
            name='product_id',
            field=models.CharField(default='-1', max_length=13),
        ),
        migrations.AddField(
            model_name='cart_item',
            name='total_ord',
            field=models.CharField(default='0', max_length=3),
        ),
    ]
