from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from user.models import User


@login_required
def update_profile(request, pk):
    user = get_object_or_404(User, pk)
    if request.methodd == 'POST':
        pass



def profile(request):
    if  not request.user.is_authenticated:
        return redirect('login')
    else: 
        user = request.user
        favorite_books = user.favorite_books.all()
        return render(request, "profile.html",{'user': user, 'favorite_books': favorite_books,})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Передаем данные формы
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:  # Для GET-запроса
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request, user)
            return redirect('index')
    elif request.method == 'GET':
        form = AuthenticationForm()

    return render(request, "login.html", context = {'form': form},)        

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')