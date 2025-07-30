from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, CustomUser
from .serializers import ProductListSerializer, ProductDetailSerializer, CategoryListSerializer, CategoryDetailSerializer

# Create your views here.
def hello(request):
    return HttpResponse('holaa')

#el decorador @api_view permite que la vista pueda recibir peticiones HTTP
@api_view(['GET'])
def product_list(request):
    product = Product.objects.filter(featured=True) 
    serializer = ProductListSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug) #compara 
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
    
    serializer = ProductDetailSerializer(product) #en este caso espera solo 1 producto
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all() #trae todas las categorias
    serializer = CategoryListSerializer(categories, many=True) #serializa todas las categorias
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)

