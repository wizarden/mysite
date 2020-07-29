from django.contrib import admin
from .models import Item, ProductImage, Product, ProductCategory


# Register your models here.


admin.site.register(Item)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(ProductCategory)
