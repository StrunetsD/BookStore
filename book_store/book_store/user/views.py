from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserRegistrationForm
from user.models import User
from django.http import HttpResponseForbidden

class UpdateProfileView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')  
        user = get_object_or_404(User, pk=pk)
        return render(request, 'update_profile.html', {'user': user})

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')  
        user = get_object_or_404(User, pk=pk)
        return redirect('profile') 

class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login') 
        user = request.user
        favorite_books = user.favorite_books.all()
        return render(request, "profile.html", {'user': user, 'favorite_books': favorite_books})

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request, "login.html", {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')