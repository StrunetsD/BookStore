from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Book, Basket

class AddToBasketView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        user = request.user
        book = get_object_or_404(Book, id=book_id)
        basket_item, created = Basket.objects.get_or_create(user=user, book=book)
        
        if created:
            basket_item.quantity = 1
        else:
            basket_item.quantity += 1
        
        basket_item.save()
        return redirect('index')

class DeleteFromBasketView(LoginRequiredMixin, View):
    def post(self, request, basket_id):
        user = request.user
        basket_item = get_object_or_404(Basket, id=basket_id, user=user)
        basket_item.delete()
        return redirect('basket')

class BasketView(LoginRequiredMixin, View):
    def get(self, request):
        basket = Basket.objects.filter(user=request.user)
        total_cost = sum(item.book.price * item.quantity for item in basket)
        context = {
            'basket_items': basket,
            'total_cost': total_cost,
        }
        return render(request, 'basket.html', context)

class UpdateCartView(LoginRequiredMixin, View):
    def post(self, request, basket_item_id):
        basket_item = get_object_or_404(Basket, id=basket_item_id, user=request.user)
        quantity = request.POST.get('quantity')

        if quantity.isdigit() and int(quantity) > 0:
            basket_item.quantity = int(quantity)
            basket_item.save()
        
        return redirect('basket')