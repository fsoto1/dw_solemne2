from django.shortcuts import render
from .models import Noticia
# Create your views here.

def index(request):
	all_noticia = Noticia.objects.all()[:6]
	destacada = Noticia.objects.filter(destacada=1)[:1]
	return render(request, 'noticias/home.html', {'all_noticia': all_noticia, 'destacada': destacada})

def detalle(request):
	query = request.GET.get("id")
	if query:
		noticia = Noticia.objects.get(id = query)
	return render(request, 'noticias/noticia_detalle.html', {'noticia': noticia})