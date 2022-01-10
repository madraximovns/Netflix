from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from film.views import ActorViewSet, MovieViewSet, CommentApiView

router = DefaultRouter()
router.register('actors', ActorViewSet)
router.register('movies', MovieViewSet, 'comments')
urlpatterns = [
    path('', include(router.urls)),
    path('comments/', CommentApiView.as_view(), name='comments'),
    path('comments/<int:pk>', CommentApiView.as_view(), name='comments'),
    path('auth/', obtain_auth_token)
]



