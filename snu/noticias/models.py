from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField

def upload_location(instance, filename):
		return "%s/%s" %(instance.id, filename)

class Categoria(models.Model):
		nombre_categoria = models.CharField(max_length=50)
		creacion = models.DateTimeField(auto_now_add=True)
		modificacion = models.DateTimeField(auto_now=True)
		def __unicode__(self):
			return self.nombre_categoria

		def __str__(self):
			return self.nombre_categoria

		class Meta:
			ordering = ["nombre_categoria"]

class Noticia(models.Model):
		titulo = models.CharField(max_length=150)
		contenido = models.TextField()
		imagen = models.ImageField(upload_to="", null=True, blank=True, width_field='ancho_imagen',height_field='alto_imagen')
		alto_imagen = models.IntegerField(default=0)
		ancho_imagen = models.IntegerField(default=0)
		fecha = models.DateField()
		categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
		destacada = models.BooleanField()
		creacion = models.DateTimeField(auto_now_add=True)
		modificacion = models.DateTimeField(auto_now=True)

		def __unicode__(self):
			return self.titulo

		def __str__(self):
			return self.titulo

		class Meta:
			ordering = ["-fecha"]