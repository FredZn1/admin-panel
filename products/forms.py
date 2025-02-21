from django import forms
from categories.models import Category
from products.models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Enter Product Name'
            }),
            'category': forms.Select(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
                'rows': '3'
            }),
            'image': forms.FileInput(attrs={
                'class': 'mt-1 block w-full',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError("Mahsulot nomi kamida 3 ta belgi bo'lishi kerak.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Narx musbat bo'lishi kerak.")
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise ValidationError("Tavsif kamida 10 ta belgidan iborat bo'lishi kerak.")
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Faqat PNG, JPG va JPEG rasm formatlari ruxsat etiladi.")
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Rasm hajmi 5MB dan oshmasligi kerak.")
        return image
