from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=200)
    picture = models.URLField()
    birthdate = models.DateField()

    def __str__(self):
        return self.name
