from django.shortcuts import render
from .models import Product, ProductCategory, Slider
from django.http import HttpResponse
from .forms import ProductForm

# Create your views here.



from django.http import HttpResponse




#return HttpResponse("123")

def index3(request):
    form = ProductForm()
    return render(request, 'base/index.html', {'form': form})



def index(request):
    form = ProductForm()
    product_list = Product.objects.order_by('name')
    category_list = ProductCategory.objects.order_by('name')
    slider_list = Slider.objects.order_by('slider_title')
    
    
    return render(request,'base/index.html', locals())


def category(request):
    
    print(request.method)
    print(request.GET)
    print(request.POST)
    
    return render(request,'base/category.html', locals())

