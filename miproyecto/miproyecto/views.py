from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse ("hola simon")

def contacto(request):
    return HttpResponse ("datos de contacto")

def servicio(request):
    var = "programador"
    return HttpResponse (var)

def eldoble(request,numero):
    
    return HttpResponse (int(numero)*2)

def eldobleqp(request,numero):
 
    numero_param = int(request.GET.get('numero', None))
    return HttpResponse (int(numero)*numero_param)

def probando_template(request):

    # Abrimos el archivo html
    mi_html = open('./plantillas/template1.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)