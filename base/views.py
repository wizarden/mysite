from django.shortcuts import render
from .models import Product, ProductCategory, Slider
from django.http import HttpResponse
# Create your views here.



from django.http import HttpResponse


def index2(request):
    my="my22"
    print(2)
    
    return render(request,'base/index2.html', locals())

def index3(request):
    print(3)
 #   print(request.GET)
 #   print(request.POST)
    my="my3"
    return render(request,'base/index2.html', locals())



#return HttpResponse("123")

def index(request):
    product_list = Product.objects.order_by('name')
    category_list = ProductCategory.objects.order_by('name')
    slider_list = Slider.objects.order_by('slider_title')
    
    
    return render(request,'base/index.html', locals())


def category(request):
    
    print(request.method)
    print(request.GET)
    print(request.POST)
    
    return render(request,'base/category.html', locals())

