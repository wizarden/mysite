from django.shortcuts import render
from .models import Product, ProductCategory, Slider
# Create your views here.


from django.http import HttpResponse


def index(request):
    product_list = Product.objects.order_by('name')
    category_list = ProductCategory.objects.order_by('name')
    slider_list = Slider.objects.order_by('slider_title')
    
    
    return render(request,'base/index.html', locals())




