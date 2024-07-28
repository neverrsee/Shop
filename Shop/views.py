from django.shortcuts import render
from .models import Product, Order


# Create your views here.

def catalog(request):
    products = Product.objects.all()
    return render(request, 'Shop/catalog.html', {'products':products})

def orders(request):
    orders = Order.objects.all()
    return render(request, 'Shop/orders.html', {'orders':orders})

def order_create(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'Shop/order_create.html', {'product':product})

def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'Shop/product_detail.html', {'product':product})
