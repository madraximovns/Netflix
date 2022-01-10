from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from film.models import Movie, Actor, Comment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            'id', 'name', 'picture', 'birthdate',

        ]

    def validate_birthdate(self, value):
        if value.year < 1950:
            raise ValidationError(detail="Must be greater than 1950")
        return value


class MovieSerializer(serializers.ModelSerializer):
    # actor = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'movie_url', 'actor']


class CommentSerializer(MovieSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'text', 'movie_id']


