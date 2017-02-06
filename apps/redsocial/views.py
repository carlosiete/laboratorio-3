from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from apps.redsocial.forms import usuario_form 

from rest_framework import viewsets, status
from apps.redsocial.models import usuario, comentario, publicacion, canal, area_conocimiento
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
	queryset = usuario.objects.all()
	serializer_class = usuarioSerializer