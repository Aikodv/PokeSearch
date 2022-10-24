from django.http import HttpResponse
import datetime 
def prueba(request):
    return HttpResponse("Hola xd")

def prueba2 (request):
    return HttpResponse("a")

def fecha(request):
    
    fecha_actual = datetime.datetime.now()
    
print(datetime.datetime.now())