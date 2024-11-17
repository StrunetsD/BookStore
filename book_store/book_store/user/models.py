from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    favorite_books = models.ManyToManyField('book.Book', blank=True)  


    def __str__(self):
        return self.username
