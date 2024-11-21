from django.urls import path
from .views import AddToBasketView, DeleteFromBasketView, BasketView, UpdateCartView

urlpatterns = [
    path('add_to_basket/<int:book_id>/', AddToBasketView.as_view(), name='add_to_basket'),
    path('delete_from_basket/<int:basket_id>/', DeleteFromBasketView.as_view(), name='delete_from_basket'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('update_cart/<int:basket_item_id>/', UpdateCartView.as_view(), name='update_cart'),
]