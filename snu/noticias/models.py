from django.db import models

class Categoria(models.Model):
	nombre_categoria = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre_categoria

	def __str__(self):
		return self.nombre_categoria

class Noticia(models.Model):
	titulo = models.CharField(max_length=50)
	contenido = models.TextField()
	imagen = models.ImageField(null=True, blank=True, width_field='ancho_imagen',height_field='alto_imagen')
	alto_imagen = models.IntegerField(default=0)
	ancho_imagen = models.IntegerField(default=0)
	fecha = models.DateField()
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.titulo

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ["fecha"]

class Destacada(models.Model):
	noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
	fecha_destacada = models.DateField()

	def __unicode__(self):
		return self.fecha_destacada

	def __str__(self):
		return  self.fecha_destacada 

	class Meta:
		ordering = ["fecha_destacada"]