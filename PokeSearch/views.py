from django.http import HttpResponse
import datetime 
def prueba(request):
    return HttpResponse("<html><head><title>Esta es mi primera pagina</title></head><body><h1>Esto es un encabezado</h1><p>Y esto es un parrafo, donde podemos escribir todo el rollo que se nos ocurra.</body></html>")

def prueba2 (request):
    return HttpResponse("a")

def fecha(request):
    
    fecha_actual = datetime.datetime.now()
    return HttpResponse(fecha_actual)
    
print(datetime.datetime.now())