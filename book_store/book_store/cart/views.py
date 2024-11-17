from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def add_to_basket(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id)
    basket_item, created = Basket.objects.get_or_create(user=user, book=book)
    if created:
        basket_item.quantity = 1
    else:
        basket_item.quantity += 1

    basket_item.save()
    return redirect('index')

@login_required
def delete_from_basket(request,basket_id):
    user = request.user
    basket_intem = get_object_or_404(Basket,id=basket_id,user=user)
    basket_intem.delete()
    return redirect('basket')

@login_required
def basket(request):
    basket = Basket.objects.filter(user=request.user)
    cost = sum(item.book.price * item.quantity for item in basket)
    context = {
        'basket_items': basket,
        'total_cost':   cost,
    }
    return render(request, 'basket.html', context)

@login_required
def update_cart(request,basket_item_id):
    basket_item = get_object_or_404(Basket,id = basket_item_id,user=request.user)
    if request.method =='POST':
        quantity = request.POST['quantity']
        if quantity.isdigit() and int(quantity)>0:
            basket_item.quantity = quantity
            basket_item.save()
        return redirect('basket')
