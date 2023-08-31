# Generated by Django 4.2.4 on 2023-08-15 12:48

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ForeignKey(default=accounts.models.Avatar.get_default, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.avatar', verbose_name='Аватар'),
        ),
    ]