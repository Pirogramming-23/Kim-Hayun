from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    stars = models.FloatField()
    runtime = models.IntegerField() 
    review = models.TextField()
    director = models.CharField(max_length=100)
    actors = models.TextField()