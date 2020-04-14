from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    image = models.CharField(max_length=100000000)
    genre = models.CharField(max_length=100000000000)
    actors = models.CharField(max_length=10000000000)
    director = models.CharField(max_length=100000000)
    vote = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    score = models.CharField(max_length=100000, blank=True)