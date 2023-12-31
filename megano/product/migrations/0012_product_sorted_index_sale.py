# Generated by Django 4.2.4 on 2023-08-29 13:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0011_remove_product_name_alter_product_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="sorted_index",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sale",
                    models.IntegerField(
                        blank=True,
                        db_index=True,
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(99),
                        ],
                        verbose_name="Скидка в %",
                    ),
                ),
                ("dateTo", models.DateTimeField(blank=True, null=True)),
                ("dateFrom", models.DateTimeField(default="")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                        verbose_name="sale_products",
                    ),
                ),
            ],
        ),
    ]
