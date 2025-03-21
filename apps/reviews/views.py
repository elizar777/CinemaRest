from django.forms import ValidationError
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny



from apps.movies.models import Movie
from apps.reviews.models import Review
from apps.reviews.permissions import ProductPermission
from apps.reviews.serializers import ReviewSerializer


class ReviewAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return (IsAuthenticated(), )
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ProductPermission(), )
        if self.action == 'create':
            return (IsAuthenticated(), )  
        if self.action == 'list':  
            return (AllowAny(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        user = self.request.user
        movie = serializer.validated_data.get('movie')

        if not Movie.objects.filter(pk=movie.pk).exists():
            raise ValidationError({'detail': 'Такого фильма не существует.'})

        if Review.objects.filter(user=user, movie=movie).exists():
            raise ValidationError({'detail': 'Вы уже оставили отзыв на этот фильм.'})

        serializer.save(user=user)
