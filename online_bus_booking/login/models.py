from django.db import models

# Create your models here.


class userRecord(models.Model):
    username = models.CharField(max_length=25,primary_key=True)
    password = models.CharField(max_length=15,null=False)
    email = models.EmailField(max_length=25,blank=True,null=True)
    mobileNumber = models.CharField(null=False,max_length=10)
    address = models.TextField(blank=True)
    dateOfBirth = models.DateField()

