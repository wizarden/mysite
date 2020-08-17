from django.shortcuts import render
from django.http import HttpResponse
from .models import Order,ProductInOrder, Product
from base.models import Product, ProductCategory, Slider
from .forms import ProductInOrderForm


def order(request):

    order_list = ProductInOrder.objects.all()

    for t in order_list:
        print(t.product.category.name)

    #product_list = Product.objects.order_by('name')[:2]
    #category_list = ProductCategory.objects.order_by('name')[:2]
    #slider_list = Slider.objects.order_by('slider_title')[:2]

    form = ProductInOrderForm()
    

    return render(request,'base/index2.html', locals())
