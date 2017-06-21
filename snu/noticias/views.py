from django.shortcuts import render
from .models import Noticia
# Create your views here.

def index(request):
	all_noticia = Noticia.objects.all()[:6]
	destacada = Noticia.objects.filter(destacada=1)[:1]
	#all_socios = all_socios.filter()
	#query = request.GET.get("q")
	#if query:
	#	all_socios = all_socios.filter(
	##		Q(rut_socios__icontains=query) |
	#		Q(nom_socios__icontains=query) |
	#		Q(apel_pat_socios__icontains=query) |
	#		Q(apel_mat_socios__icontains=query)
	#		).distinct()
	
		
		#return render(request,'socios/buscar_socios.html', {'all_socios': all_socios} )
	return render(request, 'noticias/home.html', {'all_noticia': all_noticia, 'destacada': destacada})

def detalle(request):
	query = request.GET.get("id")
	if query:
		noticia = Noticia.objects.get(id = query)
	return render(request, 'noticias/noticia_detalle.html', {'noticia': noticia})