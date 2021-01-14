from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm

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
