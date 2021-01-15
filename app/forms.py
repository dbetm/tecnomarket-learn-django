from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto, Producto


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        # fields = ['nombre', 'correo', 'tipo_consulta', 'mensaje', 'avisos']
        fields = '__all__' # all fields


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

        current_year = datetime.now().year

        widgets = {
            'fecha_fabricacion': forms.SelectDateWidget(
                years=reversed(range(current_year - 100, current_year + 1))
            )
        }


class CustomUserCreationForm(UserCreationForm):
    # Define fields to use

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
