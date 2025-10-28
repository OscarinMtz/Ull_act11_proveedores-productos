from django.contrib import admin
from .models import Proveedor, Producto

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'correo', 'direccion_corta']
    search_fields = ['nombre', 'correo']
    list_filter = ['nombre']
    
    def direccion_corta(self, obj):
        return obj.direccion[:50] + '...' if len(obj.direccion) > 50 else obj.direccion
    direccion_corta.short_description = 'Dirección'

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'proveedor', 'tiene_imagen']
    list_filter = ['proveedor', 'stock']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio', 'stock']
    
    def tiene_imagen(self, obj):
        return "✅" if obj.imagen else "❌"
    tiene_imagen.short_description = 'Imagen'