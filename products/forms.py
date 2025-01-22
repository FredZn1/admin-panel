from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'descriptions', 'image']
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'descriptions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product description',
                'rows': 5
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
