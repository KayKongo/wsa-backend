# Generated by Django 5.0.6 on 2024-06-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_remove_cart_cart_id_remove_category_category_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.CharField(max_length=255),
        ),
    ]