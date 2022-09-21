from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()