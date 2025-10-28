from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Proveedor")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    direccion = models.TextField(verbose_name="Dirección")
    logo = models.ImageField(upload_to='logos_proveedores/', blank=True, null=True, verbose_name="Logo")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Stock Disponible")
    imagen = models.ImageField(upload_to='imagenes_productos/', blank=True, null=True, verbose_name="Imagen del Producto")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos', verbose_name="Proveedor")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']