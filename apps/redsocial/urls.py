from django.conf.urls import url, include

from apps.redsocial.views import login
from apps.redsocial.views import registroView
from apps.redsocial.views import flotView
from apps.redsocial.views import inicioView
from apps.redsocial.views import usuarioViewSet

urlpatterns = [
    url(r'^$', login),
    url(r'registro', registroView),
    url(r'flot',flotView),
    url(r'inicio', inicioView),
]