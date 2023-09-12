<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm, BusquedaForm


def pagina_de_inicio(request):
    return render(request, 'pagina_de_inicio.html')


def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            # Realiza la búsqueda en la base de datos
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})
=======
from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm, BusquedaForm

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            # Realiza la búsqueda en la base de datos
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})
>>>>>>> e05f3afa8eee2925a874c67edb117784999d16ab
