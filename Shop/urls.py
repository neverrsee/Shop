from .views import *
from django.urls import path

urlpatterns = [
    path('', catalog, name='catalog'),
    path('orders/', orders, name='orders'),
    path('order_create/', order_create, name='order_create'),
    path('product/<int:product_id>', product_detail, name='product_detail')
]