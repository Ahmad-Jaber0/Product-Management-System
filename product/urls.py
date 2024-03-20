from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    
]