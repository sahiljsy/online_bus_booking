# Generated by Django 3.1.5 on 2021-03-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0012_auto_20210131_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='available_seat',
            field=models.IntegerField(null='False'),
            preserve_default='False',
        ),
    ]
