# Generated by Django 4.2.4 on 2023-08-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_alter_product_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="name",
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название"),
        ),
    ]
