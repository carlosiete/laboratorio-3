"""redsocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from apps.redsocial.views import usuarioViewSet, perfilViewSet, timeLine_canalViewSet, timeLine_publicoViewSet,timeLine_privadoViewSet, canalViewSet, area_conocimientoViewSet

router = routers.DefaultRouter()
router.register(r'usuario', usuarioViewSet)
router.register(r'canal', canalViewSet)
router.register(r'areas', area_conocimientoViewSet)
router.register(r'timeline', timeLine_publicoViewSet, 'username')
router.register(r'usuarios', timeLine_privadoViewSet)
router.register(r'canales', timeLine_canalViewSet)
router.register(r'perfil', perfilViewSet, 'perfil')



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include ('apps.redsocial.urls', namespace="redsocial")),
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/',include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]