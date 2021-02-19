from django.db import models


# Create your models here.
class AwardNominee(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=55)
    image = models.CharField(max_length=30)
    votes = models.IntegerField()
