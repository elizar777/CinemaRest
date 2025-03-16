from django.contrib import admin

from apps.movies.models import Movie

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "release_date", "genre")