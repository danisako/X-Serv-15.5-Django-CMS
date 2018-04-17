from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages




def index(request):

	respuesta = "<h2>Lista de páginas: </h2></br>"
	paginas = Pages.objects.all()
	
	for p in paginas:
		respuesta += "Nombre de pagina:" + p.name + "</br><li>contenido:" +str(p.page) + "    <li>ID:"+str(p.id)+"</br>"
		respuesta += "<li><a href=" + str(p.id) + ">Enlace a la página de: " + p.name + "</a></li><br>"
		
	return HttpResponse(respuesta)


def muestra(request,idpagina):
	
	try:
		pagina = Pages.objects.get(id = idpagina)
		respuesta = pagina.page
	except Pages.DoesNotExist:
		respuesta = "Error"

	return HttpResponse(respuesta)
