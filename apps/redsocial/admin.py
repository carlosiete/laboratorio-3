from django.contrib import admin

from apps.redsocial.models import canal, area_conocimiento, usuario

# Register your models here.
admin.site.register(canal)
admin.site.register(area_conocimiento)
admin.site.register(usuario)