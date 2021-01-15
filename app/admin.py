from django.contrib import admin

from .forms import ProductoForm
from .models import Marca, Producto, Contacto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'nuevo', 'marca']
    search_fields = ['nombre']
    list_filter = ['marca', 'nuevo']
    # pagination
    list_per_page = 10

    form = ProductoForm

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
