# Generated by Django 4.2.4 on 2023-08-29 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0012_product_sorted_index_sale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sale_products",
                to="product.product",
            ),
        ),
    ]
