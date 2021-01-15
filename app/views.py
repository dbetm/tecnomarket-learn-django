from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, CustomUserCreationForm, ProductoForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'app/home.html', context=data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto guardado'
        else:
            data['form'] = formulario
            data['mensaje'] = formulario.errors

    return render(request, 'app/contacto.html', context=data)

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto agregado correctamente.')
        else:
            data['form'] = formulario
            data['mensaje'] = formulario.errors

    return render(request, 'app/producto/agregar.html', context=data)

def listar_productos(request):
    productos = Producto.objects.all()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)
    except Exception as e:
        raise Http404

    data = {
        'productos': productos,
        'paginator': paginator
    }

    return render(request, 'app/producto/listar.html', context=data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(
            data=request.POST,
            instance=producto,
            files=request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto modificado correctamente.')
            return redirect(to='listar_productos')
        data['form'] = formulario
        data['mensaje'] = formulario.errors

    return render(request, 'app/producto/modificar.html', context=data)

def eliminar_producto(request, id):
    producto =get_object_or_404(Producto, id=id)
    producto.delete()

    messages.success(request, 'Producto eliminado correctamente.')

    return redirect(to='listar_productos')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            # authenticate
            user = authenticate(
                username=formulario.cleaned_data['username'],
                password=formulario.cleaned_data['password1']
            )
            login(request, user)
            messages.success(request, 'Te has registrado correctamente.')

            return redirect(to='home')

        data['form'] = formulario

    return render(request, 'registration/registro.html', context=data)
