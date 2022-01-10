from django.db import models
from django.contrib.auth import get_user_model
from film.models import Movie

User = get_user_model()


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=300)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

