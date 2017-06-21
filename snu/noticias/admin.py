from django.contrib import admin
from .models import Categoria, Noticia, Destacada

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria')

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha','categoria')

class DestacadaAdmin(admin.ModelAdmin):
    list_display = ('noticia','fecha_destacada','categoria')

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Destacada)