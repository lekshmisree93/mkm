from django.db import models

class book(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2500)
    price = models.FloatField()
    description = models.CharField(max_length=3000)

# Create your models here.
