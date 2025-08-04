from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem, Product, Category
from .serializers import CartItemSerializer, CartSerializer, ProductListSerializer, ProductDetailSerializer, CategoryListSerializer, CategoryDetailSerializer

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


@api_view(["POST"]) #el decorador permite recibir peticiones POST
def add_to_cart(request):
    cart_code = request.data.get("cart_code")
    product_id = request.data.get("product_id")
    
    cart, created = Cart.objects.get_or_create(cart_code=cart_code) #busca en la tabla cart, si existe, si no lo crea
    product = Product.objects.get(id=product_id)
    
    cartitem, created = CartItem.objects.get_or_create(product = product, cart = cart) # lo mismo 
    cartitem.quantity = 1

        
    cartitem.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data)

