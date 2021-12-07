from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.TextField()
    adult = models.BooleanField()
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    poster_path = models.TextField()
    release_date = models.TextField()
    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)
    original_title = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    def __str__(self):
        return self.title


# class Worldcup(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='players')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


