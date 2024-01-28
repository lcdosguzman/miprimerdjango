from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def home(request):
    mi_html = open('./templates/template1.html')
    plantilla = Template(mi_html.read())
    mi_html.close()
    plantilla = loader.get_template('template1.html')
    mi_contexto = Context()
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)

def aboutme(request):
    return HttpResponse ("Yo soy Simon")

def works(request):
    anios = [2016,2017,2018,2019,2020,2021,2022,2023,2024]
    diccionario = {"anios":anios}
    plantilla = loader.get_template('template2.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def contact(request):
    ciudad = "Buenos Aires"
    pais = "Argentina"
    anios = [2016,2017,2018,2019,2020,2021,2022,2023,2024]
    diccionario = {"ciudad":ciudad,"pais":pais,"anios":anios}
    plantilla = loader.get_template('template3.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

