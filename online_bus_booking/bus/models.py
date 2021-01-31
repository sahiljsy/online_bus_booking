from django.db import models

# Create your models here.


class Bus(models.Model):
    bus_id = models.IntegerField(null='False')
    bus_number = models.CharField(max_length=10, null='False')
    type = models.CharField(max_length=10, null='False')
    source = models.CharField(max_length=15)
    destination = models.CharField(max_length=15)
    no_of_seats = models.IntegerField(default=30, null='False')
    dep_time = models.TimeField()
    arr_time = models.TimeField()
    pricePerSeat = models.IntegerField()









