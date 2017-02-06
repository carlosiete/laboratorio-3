from django.db import models

# Create your models here.


class area_conocimiento(models.Model):
	descripcion = models.TextField()
	estatus = models.TextField(max_length=1)

class usuario(models.Model):
	id_usuario = models.TextField(primary_key=True)
	nombre = models.TextField()
	apellido = models.TextField()
	carrera = models.TextField()
	promocion = models.TextField()
	sexo = models.TextField()
	fecha_nacimiento = models.DateField()
	correo = models.TextField(unique=True)
	telefono = models.TextField(max_length=11)
	clave = models.TextField(blank=False,null=False)
	estatus = models.TextField(max_length=1)
	imagen = models.ImageField(null=True)
	area = models.ManyToManyField(area_conocimiento)

class publicacion(models.Model):
	id_usuario = models.ForeignKey(usuario, editable=True, related_name='publicacion')
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	tipo = models.TextField()

class comentario(models.Model):
	id_usuario = models.ForeignKey(usuario, editable=True, related_name='comentario')
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)	

class canal(models.Model):
	id_usuario = models.ForeignKey(usuario, editable=True, related_name='canal')
	descripcion = models.TextField()
	estatus = models.TextField(max_length=1)
	area = models.ManyToManyField( area_conocimiento)

#class canal_area(models.Model):
#	id_canal = models.ForeignKey(canal, editable=True, related_name = 'canalArea')	
#	id_area = models.ForeignKey(area_conocimiento, editable=True, related_name = 'canalArea')

class seguimiento(models.Model):
	id_seguidor = models.TextField()
	id_seguido = models.TextField()	

#class usuario_area(models.Model):
#	id_usuario = models.TextField()
#	id_area = models.TextField()

