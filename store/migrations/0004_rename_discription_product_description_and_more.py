# Generated by Django 5.0.1 on 2024-01-08 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20240105_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
