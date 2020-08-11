from django.shortcuts import render
from django.http import HttpResponse
from .models import Order,ProductInOrder



def order(request):

    order_list = ProductInOrder.objects.all()

    for t in order_list:
        print(t.product.category.name)

    return HttpResponse("123")
