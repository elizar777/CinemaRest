from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, AllowAny

# Create your views here.

from apps.movies.models import Movie
from apps.movies.serializers import MovieSerializers

class MovieAPI(GenericViewSet,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    