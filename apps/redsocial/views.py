from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from rest_framework import viewsets, status
from apps.redsocial.models import User,perfil, comentario, publicacion, canal, area_conocimiento, seguimiento
from apps.redsocial.serializers import seguimientoSerializer,perfilSerializer,  publicacionSerializer, usuarioSerializer, canalSerializer, area_conocimientoSerializer, comentarioSerializer
from rest_framework.response import Response
import json

# Create your views here.

def login(request):
	return render(request, 'redsocial/login.html')

def flotView(request):
		return render(request, 'redsocial/flot.html')	

def inicioView(request):
		return render(request, 'redsocial/inicio.html')	

def registroView(request):
		return render(request, 'redsocial/registro.html')
def compañerosView(request):
		return render(request, 'redsocial/compañeros.html')		
#hechas por edo
def inboxView(request):
		return render(request, 'redsocial/inbox.html')
def seguidosView(request):
		return render(request, 'redsocial/seguidos.html')
def seguidoresView(request):
		return render(request, 'redsocial/seguidores.html')
def mensajesView(request):
		return render(request, 'redsocial/mensajes.html')
def editarView(request):
		return render(request, 'redsocial/editar_perfil.html')


class usuarioViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('id')
	serializer_class = usuarioSerializer
	
	def retrieve(self, request, pk):
		queryset = User.objects.get(username=pk)
		print(queryset.username)
		serializer = usuarioSerializer(queryset)
		return Response(serializer.data)	

#Listar todos los canales y crear canal nuevo
class canalViewSet(viewsets.ModelViewSet):
	queryset = canal.objects.all()
	serializer_class = canalSerializer

	def create(self, request):
		json_data = json.loads(request.body.decode('utf-8'))


		username = json_data['usuario']

		usuario = None
		error_message = ''

		try:
			usuario = User.objects.get(username=username)
		except Exception as e:
			error_message = str(e)

		if (usuario != None):
			new_canal = canal()
			new_canal.usuario = usuario
			new_canal.descripcion = json_data['descripcion']		       
			new_canal.save()
			new_canal.area = json_data['area']	


			return Response({'ok' : 'true'})
		else:
			return Response({'ok' : 'false', 'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)			

class area_conocimientoViewSet(viewsets.ModelViewSet):
	queryset = area_conocimiento.objects.all()
	serializer_class = area_conocimientoSerializer

class perfilViewSet(viewsets.ModelViewSet):
	#queryset = perfil.objects.get(usuario=self.request.user)
	#serializer_class = perfil			
	def list(self, request):
		queryset = perfil.objects.get(usuario=self.request.user)
		serializer_class = perfilSerializer	


#Timeline Publico donde se muestran todas las publicaciones de tipo publicas y que no pertenecen a ningun canal
class timeLine_publicoViewSet(viewsets.ModelViewSet):
	queryset = publicacion.objects.filter(tipo="publico",canal=0)
	serializer_class = publicacionSerializer

	def create(self, request):
		json_data = json.loads(request.body.decode('utf-8'))

		username = self.request.user
		print(username)
		usuario = None
		can = 0
		error_message = ''

		try:
			usuario = User.objects.get(username=username)
			can = canal.objects.get(id=json_data['canal'])
			can = can.id
			print(can)
		except Exception as e:
			error_message = str(e)

		if (usuario != None):
			new_publicacion = publicacion()
			new_publicacion.usuario = usuario
			new_publicacion.canal = can
			new_publicacion.contenido = json_data['contenido']
			new_publicacion.tipo = json_data['tipo']		       
			new_publicacion.save()

			return Response({'ok' : 'true'})
		else:
			return Response({'ok' : 'false', 'error' : error_message},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Timeline Privado donde se muestran las publicaciones generadas por determinado usuario, solo si el usuario lo esta siguiendo
class timeLine_privadoViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = usuarioSerializer
	def retrieve(self, request, pk):
		queryset = publicacion.objects.all()
		serializer_class = publicacionSerializer		
		user = User.objects.get(username=pk)		
		queryset = publicacion.objects.filter(usuario=user, canal=0)		
		#print(queryset)
		print(self.request.user)
		print(pk)

		seguidor = self.request.user
		seguido = pk

		#se busca el usuario que esta logeado y el usuario del perfil privado
		seguidor = User.objects.get(username=seguidor)
		seguido = User.objects.get(username=seguido)

		print(seguidor.id)
		print(seguido.id)

		seg = None
		try:#se determina si el usuario esta siguiendo o no al el usuario del perfil privado
			seg = seguimiento.objects.get(seguidor = seguidor.id, seguido=seguido.id)
			print(seg)
		except Exception as e:
			error_message = str(e)
		#si el usuario lo esta siguiendo, entonces muestra todas las publicaciones de ese usuario	
		if (seg != None):	
			serializer = publicacionSerializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return Response({'ok' : 'false', 'error' : error_message},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
				

#Timeline del Canal donde se muestra todas las publicaciones generadas dentro de un canal determinado
class timeLine_canalViewSet(viewsets.ModelViewSet):
	queryset = canal.objects.all()
	serializer_class = canalSerializer
	def retrieve(self, request, pk):
		queryset = publicacion.objects.all()
		serializer_class = publicacionSerializer
		can = canal.objects.get(id=pk)
		print(pk)
		print(can)		
		queryset = publicacion.objects.filter(canal=can.id)		
		print(queryset)
		serializer = publicacionSerializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		json_data = json.loads(request.body.decode('utf-8'))

		username = self.request.user
		print(username)
		usuario = None
		can = None
		error_message = ''

		try:
			usuario = User.objects.get(username=username)
			can = canal.objects.get(id=json_data['canal'])
			can = can.id
			print(can)
		except Exception as e:
			error_message = str(e)

		if (usuario != None):
			new_publicacion = publicacion()
			new_publicacion.usuario = usuario
			new_publicacion.canal = can
			new_publicacion.contenido = json_data['contenido']
			new_publicacion.tipo = json_data['tipo']		       
			new_publicacion.save()

			return Response({'ok' : 'true'})
		else:
			return Response({'ok' : 'false', 'error' : error_message},status=status.HTTP_500_INTERNAL_SERVER_ERROR)