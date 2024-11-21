from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Book

class IndexView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class AddFavoriteBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        request.user.favorite_books.add(book)
        return redirect('book_detail', pk=pk)

class DeleteFromFavoriteBooksView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        request.user.favorite_books.remove(book)
        return redirect('profile')