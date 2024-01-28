"""
URL configuration for miproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))



    path('probandotemplate/', probando_template),
    path('eldoble/<numero>', eldoble),
    path('eldoblemultiplo/<int:numero>/', eldobleqp, name='eldoble'),
def saludo(request):
    return HttpResponse ("hola simon")

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

"""
from django.contrib import admin
from django.urls import path
from miproyecto.views import aboutme,works,contact,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', home),
    path('acercade/', aboutme),
    path('trabajos/', works),
    path('contacto/', contact),
]
