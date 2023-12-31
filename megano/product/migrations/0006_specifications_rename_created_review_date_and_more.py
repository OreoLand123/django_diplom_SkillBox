# Generated by Django 4.2.4 on 2023-08-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_product_limited_edition"),
    ]

    operations = [
        migrations.CreateModel(
            name="Specifications",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Название"
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Значение"
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="review",
            old_name="created",
            new_name="date",
        ),
        migrations.RenameField(
            model_name="review",
            old_name="grade",
            new_name="rate",
        ),
    ]
