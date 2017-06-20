from django.conf.urls import url
from . import views

app_name = 'noticias' 

urlpatterns = [
	#index
	url(r'^$', views.index, name='index'),
]