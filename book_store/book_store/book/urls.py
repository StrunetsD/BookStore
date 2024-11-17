from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('book<int:pk>/',book_detail, name= 'book_detail'),
    path('book/<int:pk>/add_to_favorites/', add_favorite_book, name='add_favorite_book'),
    path('book/<int:pk>/delete_from_favorite_books/', delete_from_favorite_books, name='delete_from_favorite_books'),
    ]
