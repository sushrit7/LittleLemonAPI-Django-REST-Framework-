# Generated by Django 5.0 on 2024-01-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("LittleLemonAPI", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name="cart",
            name="unit_price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name="order",
            name="total",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=6, null=True
            ),
        ),
    ]