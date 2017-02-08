from rest_framework import serializers
from apps.redsocial.models import area_conocimiento, User, publicacion, comentario, canal, perfil



class usuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','last_name','email','password')
		ordering = ('-created',)

class perfilSerializer(serializers.ModelSerializer):
	class Meta:
		model = perfil
		fields = ('usuario','carrera','promocion','telefono','fecha_nacimiento','area','imagen')

class area_conocimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = area_conocimiento
		fields = ('descripcion','estatus')

class publicacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = publicacion
		fields = ('usuario','contenido','fecha','tipo')
		ordering = ('-created',)	

class comentarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = comentario
		fields = ('usuario','contenido','fecha')
		ordering = ('-created',)

class canalSerializer(serializers.ModelSerializer):
	class Meta:
		model = canal
		fields = ('usuario','descripcion','estatus')					
