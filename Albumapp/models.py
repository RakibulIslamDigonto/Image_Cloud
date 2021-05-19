from django.db import models

# Create your models here.

class Albums(models.Model):
    thumbnail = models.ImageField(upload_to = 'album/images/')
    title = models.CharField(max_length=400)
    discription = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)


class Images(models.Model):
    thumbnail = models.ImageField(upload_to = 'album/images/')
    discription = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)




