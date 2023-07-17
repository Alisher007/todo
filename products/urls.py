from django.contrib import admin
from django.urls import path
from .views import (
    listProduct, 
    createProduct, 
    updateProduct, 
    deleteProduct,
    detailProduct
    )

app_name = 'products'
urlpatterns = [
    path('list/', listProduct, name='list'),
    path('create/', createProduct, name='create'),
    path('update/<int:pk>/', updateProduct, name='update'),
    path('delete/<int:pk>/', deleteProduct, name='delete'),
    path('detail/<int:pk>/', detailProduct, name='detail'),
]
