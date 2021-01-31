from django.db import models

# Create your models here.
class FeedBack(models.Model):
    email = models.EmailField(max_length=25,null=False)
    ratings = models.DecimalField(decimal_places=1,max_digits=2,null=False)
    suggestions = models.TextField(blank=True)