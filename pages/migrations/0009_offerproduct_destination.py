# Generated by Django 3.2.13 on 2024-02-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_product_boron'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerproduct',
            name='destination',
            field=models.CharField(default=1, max_length=50, verbose_name='Destination'),
            preserve_default=False,
        ),
    ]