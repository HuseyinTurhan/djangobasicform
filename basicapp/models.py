from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 264)
    email = models.EmailField()
    text = models.CharField(max_length=1024)
    date = models.DateField()
    
    def __str__(self):
        return self.name