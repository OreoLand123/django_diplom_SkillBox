# Generated by Django 4.2.4 on 2023-08-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="author",
            field=models.CharField(max_length=200, verbose_name="Автор"),
        ),
        migrations.AlterField(
            model_name="review",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Почта автора"),
        ),
    ]
