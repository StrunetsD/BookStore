from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add_to_basket/<int:book_id>/', add_to_basket, name='add_to_basket'),
    path('delete_from_basket/<int:basket_id>/', delete_from_basket, name='delete_from_basket'),
    path('basket',basket, name='basket'),
    path('update_cart/<int:basket_item_id>/',update_cart, name='update_cart')
    ]
