from django.db import models

from apps.movies.models import Movie
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews')
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Отзыв'
    )
    rating = models.PositiveIntegerField(
        verbose_name='Оценка от 1 до 10'
    )
    
    def __str__(self):
        return f'{self.user.username} - {self.movie.title} ({self.rating})'