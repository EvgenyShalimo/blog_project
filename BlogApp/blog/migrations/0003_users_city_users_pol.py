# Generated by Django 4.1.4 on 2023-03-31 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_users_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='pol',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Пол'),
            preserve_default=False,
        ),
    ]