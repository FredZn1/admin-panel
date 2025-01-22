from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),  # Product list
    path('<int:pk>/', views.product_detail, name='detail'),  # Product detail
    path('create/', views.product_create, name='create'),  # Create product
    path('<int:pk>/update/', views.product_update, name='update'),  # Update product
    path('<int:pk>/delete/', views.product_delete, name='delete'),  # Delete product
]
