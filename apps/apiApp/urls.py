from django.urls import path
from . import views

urlpatterns = [
    path('produc_list', views.product_list, name='products_list'),
    path('products/<slug:slug>', views.product_detail, name='product_detail'),
    path('categoty_list', views.category_list, name='category_list'),
    path('categoty/<slug:slug>', views.category_detail, name='category_detail')
]
