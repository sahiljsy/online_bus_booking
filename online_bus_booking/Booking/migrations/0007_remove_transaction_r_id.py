# Generated by Django 3.1.5 on 2021-03-10 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0006_transaction_r_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='r_id',
        ),
    ]
