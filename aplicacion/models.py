from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Turno(models.Model):        
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField(null=False, blank=False)  
    especialidad = models.CharField(max_length=50)    
    
    def __str__(self):
        return f"{self.nombre} {self.dni} {self.especialidad}"


class Especialidad (models.Model):
    nombre = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.doctor}"


# Blog
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Avatar mi perfil
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"