"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from restapi.apps.users import views # Importa las vistas de los usuarios

router = routers.DefaultRouter() # Crea un enrutador por defecto
router.register(r'users', views.UserViewSet)  # Registra el UserViewSet
router.register(r'groups', views.GroupViewSet)  # Registra el GroupViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Incluye las URLs del enrutador
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # Incluye las URLs de autenticación de DRF
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configura las URLs para servir archivos multimedia
