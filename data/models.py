from django.db import models

# Create your models here.Create
class Data(models.Model):
    name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()