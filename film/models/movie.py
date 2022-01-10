from django.db import models
from film.models import Actor

GENRE = [
    ('r', 'romantik'),
    ('d', 'dromatik'),
    ('h', 'horror'),
    ('m', 'melodram'),
]


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(choices=GENRE, max_length=10)
    movie_url = models.URLField()
    actor = models.ForeignKey(to=Actor,on_delete=models.CASCADE, related_name='actor')
    imdb = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

