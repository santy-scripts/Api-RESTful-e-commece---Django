from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductListSerializer, ProductDetailSerializer, CategoryListSerializer, CategoryDetailSerializer

#el decorador @api_view permite que la vista pueda recibir peticiones HTTP
@api_view(['GET'])
def product_list(request):
    product = Product.objects.filter(featured=True) 
    serializer = ProductListSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug) #compara 
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

