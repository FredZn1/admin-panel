from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.category_list, name='list'),  # Category list
    path('<int:pk>/', views.category_detail, name='detail'),  # Category detail
    path('create/', views.category_create, name='create'),  # Create category
    path('<int:pk>/update/', views.category_update, name='update'),  # Update category
    path('<int:pk>/delete/', views.category_delete, name='delete'),  # Delete category
]
