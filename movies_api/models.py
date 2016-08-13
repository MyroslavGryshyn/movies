from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=200)
    year = models.CharField(max_length=30)
    director = models.CharField(max_length=200)
    imdbrating = models.CharField(max_length=200)
    poster = models.CharField(max_length=2000)
    plot = models.CharField(max_length=20000)

    class Meta:
        unique_together = (("title", "year"),)
