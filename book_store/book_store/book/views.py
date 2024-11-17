from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books':books})

def book_detail(request, pk):
        book = get_object_or_404(Book, id = pk)
        return render(request, "book_detail.html", {'book':book})
    
@login_required
def add_favorite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        user = request.user
        user.favorite_books.add(book)  
        return redirect('book_detail', pk=pk)  

    print("Request method was not POST.")
    return redirect('book_detail', pk=pk)

@login_required
def delete_from_favorite_books(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
         request.user.favorite_books.remove(book)
         return redirect('profile')
    
    return redirect('profile')