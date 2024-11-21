from django.urls import path
from .views import IndexView, BookDetailView, AddFavoriteBookView, DeleteFromFavoriteBooksView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/add_favorite/', AddFavoriteBookView.as_view(), name='add_favorite_book'),
    path('book/<int:pk>/delete_favorite/', DeleteFromFavoriteBooksView.as_view(), name='delete_from_favorite_books'),
]