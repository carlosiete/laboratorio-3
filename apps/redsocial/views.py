from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from rest_framework import viewsets, status
from apps.redsocial.models import User, comentario, publicacion, canal, area_conocimiento
from apps.redsocial.serializers import publicacionSerializer, usuarioSerializer, canalSerializer, area_conocimientoSerializer, comentarioSerializer
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



class usuarioViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = usuarioSerializer
	def create_auth(request):
		serialized = UserSerializer(data=request.DATA)
		if serialized.is_valid():
			User.objects.create_user(
				serialized.init_data['email'],
				serialized.init_data['username'],
				serialized.init_data['password']
			)

			return Response(serialized.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)		

class timeLineViewSet(viewsets.ModelViewSet):
	queryset = publicacion.objects.all()
	serializer_class = publicacionSerializer

	def update(self, request, pk=None):
		pass

	def create(self, request):
		json_data = json.loads(request.body)

		username = json_data['username']

		user = None
		error_message = ''
        
		try:
			user = User.objects.get(username=username)
        
		except Exception as e:
			error_message = str(e)

		if (user != None):
			new_post = publicacion()
			new_post.contentido = json_data['contenido']
			new_post.usuario = user
			new_post.save()
			return Response({'ok' : 'true'})
		else:
			return Response({'ok' : 'false', 'error' : error_message},status=status.HTTP_500_INTERNAL_SERVER_ERROR)				