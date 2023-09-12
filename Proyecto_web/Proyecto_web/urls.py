"""
URL configuration for Proyecto_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include 
from APP_WEB import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_de_inicio, name='pagina_de_inicio'),
    path('pagina_de_inicio/', views.pagina_de_inicio, name='pagina_de_inicio'),
    path('categoria/', views.agregar_categoria, name='categoria_list'),
    path('categoria/<int:pk>/', views.agregar_categoria, name='categoria_detail'),
    path('cliente/', views.agregar_cliente, name='cliente_list'),
    path('cliente/<int:pk>/', views.agregar_cliente, name='cliente_detail'),
    path('producto/', views.agregar_producto, name='producto_list'),
    path('producto/<int:pk>/', views.agregar_producto, name='producto_detail'),
    path('buscar/', views.buscar, name='buscar'),
    path('app_web/', include('APP_WEB.urls')),  
]


from django.urls import path
from . import views

urlpatterns = [
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('buscar/', views.buscar, name='buscar'),
]
