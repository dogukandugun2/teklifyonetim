# Generated by Django 3.2.13 on 2024-02-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_offerproduct_line_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unit_price',
        ),
        migrations.AddField(
            model_name='offerproduct',
            name='offer_product_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Price (usd/ton)'),
            preserve_default=False,
        ),
    ]