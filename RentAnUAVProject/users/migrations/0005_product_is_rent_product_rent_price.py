# Generated by Django 5.0.1 on 2024-01-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_category_options_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_rent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='rent_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
