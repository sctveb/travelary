from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.urls import reverse

# Create your models here.Create
class Data(models.Model):
    
    menu = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
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

def post_image_path(instance, filename):
    return 'posts/{}/{}'.format(instance.pk, filename)
    
class Review(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    image = ProcessedImageField(
                            upload_to=post_image_path,
                            processors=[ResizeToFill(716,537)],
                            format="JPEG",
                            options={'quality':90},
                                    )
                                    
    def get_absolute_url(self):
        return reverse('data:detail', kwargs={'pk': self.data_id})
       
    