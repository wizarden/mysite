from django.shortcuts import render
from .models import Product
# Create your views here.


from django.http import HttpResponse


def index(request):
    product_list = Product.objects.order_by('name')
    
    return render(request,'base/index.html', locals())


