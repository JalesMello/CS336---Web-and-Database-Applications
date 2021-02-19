from django.db import models


# Create your models here.
class Workshop(models.Model):
    title = models.CharField(max_length=40)
    session = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
