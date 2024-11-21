from django.urls import path
from .views import UpdateProfileView, ProfileView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]