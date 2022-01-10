from django.db.models import Q
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from film.models import Movie, Actor, Comment
from film.serializers import MovieSerializer, ActorSerializer, CommentSerializer


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'actor__name']
    ordering_fields = ['imdb', '-imdb']

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        movie = self.get_queryset()
        movie = movie.order_by('-id')
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        actor_id =request.data["actor_id"]
        actor = Actor.objects.get(id=actor_id)
        movie.actor.add(actor)
        movie.save()

        return Response({"status": "Add actor Successfully"})

    @action(detail=True, methods=['DELETE'])
    def remove_actor(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data['actor_id']
        actor = Actor.objects.get(id=actor_id)
        movie.actor.remove(actor)
        movie.save()

        return Response({"status": "Remove actor Successfully"})

    @action(detail=True, methods=['GET'])
    def actors(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actor, many=True)
        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        actor = self.get_queryset()
        actor = actor.order_by('-id')
        serializer = ActorSerializer(actor, many=True)
        return Response(serializer.data)


class CommentApiView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def get(self, request):
        comments = Comment.objects.filter(user_id=request.user.id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        comments = Comment.objects.filter(Q(user_id=request.user) & Q(pk=pk))
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)