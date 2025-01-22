from django.db import models
from django.urls import reverse
from config.utils import BaseModel

class Order(BaseModel):
    customer_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created_at = models.DateField(auto_now_add=True)


    def get_detail_url(self):
        return reverse('orders:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('orders:update', args=[self.pk])

    def __str__(self):
        return f"{self.customer_name}"