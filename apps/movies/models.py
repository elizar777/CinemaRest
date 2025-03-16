from django.db import models

class Movie(models.Model):  
    title = models.CharField(
        max_length=255,  # исправлено на max_length
         verbose_name="Название фильма"
     )

    description = models.TextField(  
        verbose_name="Описание"
    )

    release_date = models.DateField(  
        verbose_name="Дата выхода"
    )

    genre = models.CharField(
         max_length=255,  # исправлено на max_length
         verbose_name="Жанр"
    )

    def __str__(self):
        return self.title
