from django.contrib import admin
from .models import Categoria, Noticia

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria')

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha','categoria')


admin.site.register(Categoria)
admin.site.register(Noticia)
