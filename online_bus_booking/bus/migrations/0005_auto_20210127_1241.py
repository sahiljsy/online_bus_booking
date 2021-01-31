# Generated by Django 3.1.5 on 2021-01-27 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_bus_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='time',
            new_name='arr_time',
        ),
        migrations.AddField(
            model_name='bus',
            name='dep_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
