from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='list'),
    path('<int:pk>/', views.order_detail, name='detail'),
    path('create/', views.order_create, name='create'),
    path('<int:pk>/update/', views.order_update, name='update'),
    path('<int:pk>/delete/', views.order_delete, name='delete'),
]
