from django.db import models
from django.urls import reverse
from config.utils import BaseModel
from categories.models import Category


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    descriptions = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
        return self.product_name

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('products:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('products:delete', args=[self.pk])





