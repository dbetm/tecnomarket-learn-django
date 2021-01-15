from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

from .models import Contacto, Producto
from .validators import MaxSizeValidator


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        # fields = ['nombre', 'correo', 'tipo_consulta', 'mensaje', 'avisos']
        fields = '__all__' # all fields


class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(
        required=False,
        validators=[MaxSizeValidator(max_file_size=2)]
    )
    precio = forms.IntegerField(min_value=1, max_value=2000000)

    # Validate unique name
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        # nombre__iexact for non-sensitive
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError('Este nombre ya existe.')

        return value

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
