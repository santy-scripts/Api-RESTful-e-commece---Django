from django.urls import path
from . import views

urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    path('/<slug:slug>', views.product_detail, name='product_detail'),
    path('category_list', views.category_list, name='category_list'),
    path('category_detail/<slug:slug>', views.category_detail, name='category_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart')
]
