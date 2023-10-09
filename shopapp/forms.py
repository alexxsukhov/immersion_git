from django import forms
from .models import Product


class EditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category_id', 'price', 'image']
