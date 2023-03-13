# Generated by Django 3.2.8 on 2023-02-25 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=64, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
    ]