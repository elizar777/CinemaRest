from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.core.cache import cache
from rest_framework.response import Response

from apps.movies.models import Movie
from apps.movies.serializers import MovieSerializers

class MovieAPI(GenericViewSet,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin):  # Добавляем mixins для обновления и удаления
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'description')
    search_fields = ('title', 'description')

    def retrieve(self, request, *args, **kwargs):
        movie_id = kwargs.get("pk")
        cache_key = f"movie_{movie_id}"  # Уникальный ключ в Redis

        # Проверяем, есть ли фильм в Redis
        movie_data = cache.get(cache_key)
        if movie_data:
            print("Данные загружены из Redis!")  # Лог
            return Response(movie_data)  # Возвращаем из кэша

        # Если нет, получаем фильм из базы
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Сохраняем в Redis на 10 минут
        cache.set(cache_key, serializer.data, timeout=600)

        print("Данные загружены из базы и сохранены в Redis!")  # Лог
        return Response(serializer.data)

    def perform_update(self, serializer):
        # Очистка кэша при обновлении фильма
        movie_id = serializer.instance.pk
        cache_key = f"movie_{movie_id}"
        cache.delete(cache_key)  # Удаляем кэш
        print("Кэш фильма удален!")  # Лог
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        # Очистка кэша при удалении фильма
        movie_id = instance.pk
        cache_key = f"movie_{movie_id}"
        cache.delete(cache_key)  # Удаляем кэш
        print("Кэш фильма удален!")  # Лог
        super().perform_destroy(instance)
 