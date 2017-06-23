from django.shortcuts import render
from .models import Noticia
from django.http import Http404
# Create your views here.

def index(request):
	all_noticia = Noticia.objects.all()[:6]
	destacada = Noticia.objects.filter(destacada=1)[:1]
	return render(request, 'noticias/home.html', {'all_noticia': all_noticia, 'destacada': destacada})

def detalle(request):
	try:
		query = request.GET.get("id")
		if query:
			noticia = Noticia.objects.get(id = query)
	except Noticia.DoesNotExist:
			raise Http404("La página no fue encontrada")
	return render(request, 'noticias/noticia_detalle.html', {'noticia': noticia})