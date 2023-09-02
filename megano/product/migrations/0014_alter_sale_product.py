# Generated by Django 4.2.4 on 2023-08-29 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0013_alter_sale_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sale_products",
                to="product.product",
            ),
        ),
    ]
