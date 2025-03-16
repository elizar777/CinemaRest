from rest_framework import serializers
from apps.reviews.models import Review


class ReviewSerializers(serializers.ModelSerializer):
    model = Review
    field = ('id', 'movie', 'users', 'text', 'rating')
    