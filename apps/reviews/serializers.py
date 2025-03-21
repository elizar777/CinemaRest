from rest_framework import serializers
from apps.reviews.models import Review
from apps.movies.models import Movie

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('movie','user', 'text', 'rating')
        
    def validate_movie(self, value):
        if not Movie.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Такого фильма не существует!")
        return value
