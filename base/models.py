from django.db import models


        

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    category_image = models.ImageField(upload_to='category_images/', blank=True, null=True, default=None )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    des = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.image

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Slider(models.Model):
    slider_title = models.CharField(max_length=64, blank=True, null=True, default=None)
    slider_description = models.TextField(blank=True, null=True, default=None)
    slider_image = models.ImageField(upload_to='category_images/', blank=True, null=True, default=None )
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.slider_title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'





