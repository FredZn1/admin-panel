from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='list'),  # Order list
    path('<int:pk>/', views.order_detail, name='detail'),  # Order detail
    path('create/', views.order_create, name='create'),  # Create order
    path('<int:pk>/update/', views.order_update, name='update'),  # Update order
    path('<int:pk>/delete/', views.order_delete, name='delete'),  # Delete order
]
