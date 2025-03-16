from rest_framework import serializers
from apps.movies.models import Movie


class MovieSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Movie
        fields = ("id", "title", "description", "release_date", "genre")
        
        
        
        