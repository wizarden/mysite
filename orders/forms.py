from django import forms
from .models import ProductInOrder


class ProductInOrderForm(forms.ModelForm):
    
    class Meta:
        model = ProductInOrder
        fields = '__all__'