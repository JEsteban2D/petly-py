from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Medico(models.Model):
    ESPECIALIDADES = [
        ('general', 'Medicina General'),
        ('cirugia', 'Cirugía'),
        ('dermatologia', 'Dermatología'),
        ('oftalmologia', 'Oftalmología'),
        ('cardiologia', 'Cardiología'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDADES)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_contratacion = models.DateField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.especialidad}"

class Mascota(models.Model):
    ESPECIES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
        ('roedor', 'Roedor'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIES)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    historial_medico = models.TextField(blank=True)
    foto = models.ImageField(upload_to='mascotas/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.especie}"

class Cita(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    notas = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cita de {self.mascota.nombre} con Dr. {self.medico.user.get_full_name()}"

class Producto(models.Model):
    CATEGORIAS = [
        ('alimento', 'Alimento'),
        ('medicamento', 'Medicamento'),
        ('accesorio', 'Accesorio'),
        ('higiene', 'Higiene'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
