from django.db import models
from django.db import connections
cursor = connections['seducla'].cursor()


class egresados(models.Model):
	cedula = models.TextField(primary_key=True)
	nombre = models.TextField()
	apellido = models.TextField()	
