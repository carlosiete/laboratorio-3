from rest_framework import serializers
from apps.redsocial.models import area_conocimiento, User, publicacion, comentario, canal, perfil, seguimiento



class usuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','first_name','last_name','email','password')

class perfilSerializer(serializers.ModelSerializer):
	class Meta:
		model = perfil
		fields = ('usuario','carrera','promocion','telefono','fecha_nacimiento','area','imagen')

class area_conocimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = area_conocimiento
		fields = ('id','descripcion', 'estatus')

class publicacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = publicacion
		fields = ('usuario','canal','contenido','fecha','tipo')
		ordering = ('-created',)	

class comentarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = comentario
		fields = ('usuario','contenido','fecha')
		ordering = ('-created',)

class canalSerializer(serializers.ModelSerializer):
	class Meta:
		model = canal
		fields = ('usuario','descripcion','area')

class seguimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = seguimiento
		fields = ('seguidor', 'seguido')							
