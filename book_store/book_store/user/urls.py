from django.urls import path
from .views import *
urlpatterns = [
   path('login/',login_view, name = 'login'),
   path('register/',register_view, name = 'register'),
   path('profile/', profile, name = 'profile'),
   path('logout/', logout_view, name ='logout')
]
