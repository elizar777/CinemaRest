from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

from apps.movies.models import Movie
from apps.movies.serializers import MovieSerializers

class MovieAPI(GenericViewSet,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'description')
    search_fields = ('title', 'description')
    