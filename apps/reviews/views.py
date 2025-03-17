from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Create your views here.

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer


class ReviewAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer