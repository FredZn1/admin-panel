from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'descriptions', 'image']
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            'descriptions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category description',
                'rows': 5
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
