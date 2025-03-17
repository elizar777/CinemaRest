from rest_framework import serializers
from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('movie','user', 'text', 'rating')
