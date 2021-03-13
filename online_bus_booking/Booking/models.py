from django.db import models


class PromoCode(models.Model):
    code = models.CharField(max_length=20)
    discount = models.FloatField()
    description = models.CharField(max_length=500)
    numberoftickets = models.IntegerField(blank=False,null=False,default=100)


class Reservation(models.Model):
    username = models.CharField(null=False, max_length=25)
    numberOfTicket = models.IntegerField(blank=True,default=0)
    dateOfJourney = models.DateField(null=True)
    bus_id = models.IntegerField(null=True)


class Transaction(models.Model):
    username = models.CharField(null=False, max_length=25)
    date = models.DateField(null=False)
    amount = models.IntegerField(null=False)
    payment_method = models.CharField(default="debit card", max_length=15, null=False)
    refund_amount = models.IntegerField(default=0, null=False)


class DebitCard(models.Model):
    username = models.CharField(null=False, max_length=25)
    cardNumber = models.PositiveIntegerField()
    cvv = models. IntegerField()
    expiry_date = models.DateField()


class UPI(models.Model):
    username = models.CharField(null=False, max_length=25)
    upi_id = models.CharField(max_length=45)
    pin = models.IntegerField()





