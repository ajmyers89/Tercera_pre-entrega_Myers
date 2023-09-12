from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_de_inicio, name='pagina_de_inicio'),
    path('categoria/', views.agregar_categoria, name='categoria_list'),
    path('categoria/<int:pk>/', views.agregar_categoria, name='categoria_detail'),
    path('cliente/', views.agregar_cliente, name='cliente_list'),
    path('cliente/<int:pk>/', views.agregar_cliente, name='cliente_detail'),
    path('producto/', views.agregar_producto, name='producto_list'),
    path('producto/<int:pk>/', views.agregar_producto, name='producto_detail'),
    path('buscar/', views.buscar, name='buscar'),
]
