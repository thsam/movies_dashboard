from django.db import models

# Create your models here.
class Movies(models.Model):
    movie=models.CharField(max_length=50)
    user=models.CharField(max_length=100)
    profilename=models.CharField(max_length=1000)
    helpfulness=models.CharField(max_length=10)
    score=models.FloatField()
    date=models.DateTimeField()
    summary=models.CharField(max_length=2000)