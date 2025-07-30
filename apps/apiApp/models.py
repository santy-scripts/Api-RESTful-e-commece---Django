from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Modelo personalizado de usuario que extiende el usuario estándar de Django
class CustomUser(AbstractUser):
    # Email único para cada usuario
    email = models.EmailField(unique=True)
    # URL opcional para la foto de perfil
    profile_picture_url = models.URLField(blank=True, null=True)

    # Representación en texto del usuario (muestra el email)
    def __str__(self):
        return self.email

# Modelo para categorías de productos
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    # Imagen opcional para la categoría
    image = models.ImageField(upload_to='category_img', blank=True, null=True)

    #funcion para mostrar el nombre de la categoría en /admin
    def __str__(self):
        return self.name


#clase producto
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='product_img', blank=True, null=True)
    featured = models.BooleanField(default=True)
    # llave primaria que relaciona el produto a una categoria
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, blank=True, null=True)

    #funcion para mostrar el nombre del producto en /admin
    def __str__(self):
        return self.name