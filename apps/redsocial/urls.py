from django.conf.urls import url, include
from apps.redsocial.views import login
from apps.redsocial.views import registroView
from apps.redsocial.views import flotView
from apps.redsocial.views import inicioView
from apps.redsocial.views import usuarioViewSet
from apps.redsocial.views import compañerosView
from rest_framework import routers


from apps.redsocial.views import inboxView #hecha por eddo
from apps.redsocial.views import mensajesView  #hecha por eddo
from apps.redsocial.views import seguidosView #hecha por eddo
from apps.redsocial.views import seguidoresView #hecha por eddo
from apps.redsocial.views import editarView #hecha por eddo


router = routers.DefaultRouter()


urlpatterns = [
    url(r'^$', login),
    url(r'registro', registroView),
    url(r'flot',flotView),
    url(r'inicio', inicioView),
    url(r'compañeros', compañerosView),
    url(r'inbox',inboxView),
    url(r'mensajes', mensajesView),
    url(r'seguidos',seguidosView),
    url(r'seguidores',seguidoresView),
    url(r'editar',editarView),

]