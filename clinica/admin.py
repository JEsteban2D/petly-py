from django.contrib import admin
from .models import Medico, Mascota, Cita, Producto

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('user', 'especialidad', 'telefono', 'activo')
    list_filter = ('especialidad', 'activo')
    search_fields = ('user__first_name', 'user__last_name', 'telefono')

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'propietario', 'peso')
    list_filter = ('especie', 'raza')
    search_fields = ('nombre', 'propietario__username')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'medico', 'fecha_hora', 'estado')
    list_filter = ('estado', 'fecha_hora')
    search_fields = ('mascota__nombre', 'medico__user__username')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}
