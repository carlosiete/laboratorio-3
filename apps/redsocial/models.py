from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class area_conocimiento(models.Model):
	descripcion = models.TextField()
	estatus = models.TextField(max_length=1)

"""class usuario(models.Model):
	id_usuario = models.TextField(primary_key=True)
	nombre = models.TextField()
	apellido = models.TextField()
	correo = models.TextField(unique=True)
	clave = models.TextField(blank=False,null=False)
	estatus = models.TextField(max_length=1)"""

class perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	carrera = models.TextField()
	promocion = models.TextField()
	telefono = models.TextField(max_length=11)
	fecha_nacimiento = models.DateField()
	imagen = models.ImageField(null=True)
	area = models.ManyToManyField(area_conocimiento)    	

class publicacion(models.Model):
	usuario = models.ForeignKey(User, editable=True, related_name='publicacion')
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	tipo = models.TextField()

class comentario(models.Model):
	usuario = models.ForeignKey(User, editable=True, related_name='comentario')
	publicacion = models.ForeignKey(publicacion, editable=True, related_name='publicacion')
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)	

class canal(models.Model):
	usuario = models.ForeignKey(User, editable=True, related_name='canal')
	descripcion = models.TextField()
	estatus = models.TextField(max_length=1)
	area = models.ManyToManyField( area_conocimiento)

class seguimiento(models.Model):
	seguidor = models.TextField()
	seguido = models.TextField()

