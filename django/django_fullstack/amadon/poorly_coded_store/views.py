from django.shortcuts import render , redirect
from .models import Order, Product
from . import models

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process_money(request):
    price = float(models.product_price(description = request.POST['price']))
    if 'quantity' not in request.session:
        request.session['quantity'] = 0
    request.session['quantity'] += int(request.POST["quantity"])
    if 'price' not in request.session :
        request.session['price'] = price*request.POST['price']
    request.session['price'] += int(request.POST["quantity"])*price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered= int(request.POST["quantity"]), total_price= int(request.POST["quantity"]) * price)
    return redirect('/checkout')

def checkout(request):
    context = {
        'quantity' :request.session['quantity'],
        'price': request.session['price'],
    }
    return render(request, "store/checkout.html",context )

def delete_session(request):
    request.session['quantity'] = 0
    request.session['price'] = 0
    return redirect('/')