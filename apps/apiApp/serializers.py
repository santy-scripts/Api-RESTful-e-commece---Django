from rest_framework import serializers

#los serializadores definen los campos que se van exponer de los modelos hechos en models.py

class ProductListSerializer(serializers.Serializer):
    class Meta:
        model = 'Product'
        fields = ['id', 'name', 'price', 'slug', 'image']
        
class ProductDetailSerializer(serializers.Serializer):
    class Meta:
        model = 'Product'
        fields = ['id', 'name', 'description', 'price', 'slug', 'image']
        
class CategoryListSerializer(serializers.Serializer):
    class Meta:
        model = 'Category'
        fields = ['id', 'name', 'slug', 'image']
        
class CategoryDetailSerializer(serializers.Serializer):
    # relacion muchos a uno (many=True)
    products = ProductListSerializer(many=True, read_only=True) 
    class Meta:
        model = 'Category'
        fields = ['id', 'name', 'product ', 'description', 'slug', 'image']