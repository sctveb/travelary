from django.db import models
from django.conf import settings


# Create your models here.Create
class Data(models.Model):
    
    menu = models.CharField(max_length=100)
    name = models.CharField(max_length=100) 
    businessCategory = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    microReview = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    options = models.CharField(max_length=100)
    totalReviewCount = models.CharField(max_length=100)
    roadAddr = models.CharField(max_length=100)
    commonAddr = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    imageSrc = models.CharField(max_length=200)
    
class review(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    image = models.ImageField()
    