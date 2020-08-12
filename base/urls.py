from django.urls import path

from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('category', views.category, name='category'),
]