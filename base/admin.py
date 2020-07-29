from django.contrib import admin
from .models import * # Item, ProductImage, Product, ProductCategory


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(Item)
admin.site.register(ProductImage)

admin.site.register(ProductCategory)
