# Generated by Django 3.2.13 on 2024-02-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20240215_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='boron',
            field=models.CharField(choices=[('added', 'added'), ('not_added', 'not_added')], default='added', max_length=50),
        ),
    ]