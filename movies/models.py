from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    year = models.CharField(max_length=32, null=True, blank=True)
    rated = models.CharField(max_length=32, null=True, blank=True)
    released = models.CharField(max_length=32, null=True, blank=True)
    runtime = models.CharField(max_length=32, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    awards = models.CharField(max_length=255, null=True, blank=True)
    imdb_rating = models.CharField(max_length=32, null=True, blank=True)
    imdb_votes = models.CharField(max_length=32, null=True, blank=True)
    imdb_id = models.CharField(max_length=32, null=True, blank=True)
    type = models.CharField(max_length=32, null=True, blank=True)
    total_seasons = models.CharField(max_length=32, null=True, blank=True)
    writer = models.TextField(null=True, blank=True)
    actors = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    poster = models.CharField(max_length=255, null=True, blank=True)
    plot = models.TextField(null=True, blank=True)
    box_office = models.CharField(max_length=255, null=True, blank=True)
    dvd = models.CharField(max_length=255, null=True, blank=True)
    metascore = models.CharField(max_length=255, null=True, blank=True)
    production = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    value = models.CharField(max_length=32)
