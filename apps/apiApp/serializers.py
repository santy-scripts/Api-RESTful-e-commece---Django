from rest_framework import serializers
from apps.apiApp.models import Cart, Category, Product, CartItem

#los serializadores definen los campos que se van exponer de los modelos hechos en models.py

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'slug', 'image']
        
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'slug', 'image']
        
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    # relacion muchos a uno (many=True)
    products = ProductListSerializer(many=True, read_only=True) 
    class Meta:
        model = Category
        fields = ['id', 'name', 'product ', 'description', 'slug', 'image']
        
        
class CartItemSerializer(serializers.ModelSerializer):
    # Representa el producto con otro serializer (más detallado que solo el ID)
    product = ProductListSerializer(read_only=True)
    # Campo calculado que no está directamente en el modelo (subtotal = precio * cantidad)
    sub_total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem 
        fields = ['id', 'product', 'quantity', 'sub_total']
        
    # Esta función calcula el subtotal de este ítem precio * cantidad
    def get_sub_total(self, CartItem):
        total = CartItem.product.price * CartItem.quantity
        return total
    

class CartSerializer(serializers.ModelSerializer):
    # Serializa todos los ítems del carrito usando CartItemSerializer (uno a muchos)
    cartitems = CartItemSerializer(read_only=True, many=True)
    # Campo calculado para obtener el total del carrito
    cart_total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'cart_code', 'cartitems', 'cart_total']
        
    # Calcula el total del carrito sumando cada subtotal de cada ítem
    def get_cart_total(self, cart):
        items = cart.cartitems.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
    

class CartStatSerializer(serializers.ModelSerializer):
    # Campo calculado que representa la cantidad total de productos en el carrito
    total_quiantity = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ["id", "cart_code", "total_quantity"]
        
     # Calcula la suma total de unidades en el carrito (sin importar el producto)
    def get_total_quantity(self, cart):
        items = cart.cartitems.all()
        total = sum([item.quantity for item in items])
        return total