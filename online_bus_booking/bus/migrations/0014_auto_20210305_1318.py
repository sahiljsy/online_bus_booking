# Generated by Django 3.1.5 on 2021-03-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0013_bus_available_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='available_seat',
            field=models.IntegerField(default=0, null='False'),
        ),
    ]
