from django.db import models


class PromoCode(models.Model):
    code = models.CharField(max_length=10)
    discount = models.FloatField()
    description = models.CharField(max_length=500)


class Reservation(models.Model):
    numberOfTicket = models.IntegerField(null='False')
    dateOfJourney = models.DateField(null='False')
    bus_id = models.IntegerField(null='False')


class Transaction(models.Model):
    username = models.CharField(null=False, max_length=25)
    date = models.DateField(null=False)
    amount = models.PositiveIntegerField(null=False)
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





