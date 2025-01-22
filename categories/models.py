from django.db import models
from django.urls import reverse
from config.utils import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='category_images', blank=True, null=True)

    def __str__(self):
        return self.category_name

    def get_detail_url(self):
        return reverse('categories:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('categories:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('categories:delete', args=[self.pk])





