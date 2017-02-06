from rest_framework import serializers
from apps.redsocial.models import area_conocimiento, usuario, publicacion, comentario, canal





class usuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = usuario
		fields = ('nombre','apellido','carrera','promocion','sexo','fecha_nacimiento','correo','telefono','clave','estatus','imagen')
		ordering = ('-created',)

class area_conocimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = area_conocimiento
		fields = ('descripcion','estatus')

class publicacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = publicacion
		fields = ('id_usuario','contenido','fecha','tipo')
		ordering = ('-created',)	

class comentarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = comentario
		fields = ('id_usuario','contenido','fecha')
		ordering = ('-created',)

class canalSerializer(serializers.ModelSerializer):
	class Meta:
		model = canal
		fields = ('id_usuario','descripcion','estatus')					
