import datetime as dt
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("<br><br><br>¡Hola mundo!<br><br>  ")

def dia(request):
    dia = dt.datetime.now()
    return HttpResponse(f"<br><br><br>La fecha y hora de hoy es {dia}<br><br>  ")

def template1(self):
    nombre = "Mariano"
    apellido = "Sirio"

    diccionario = {"Nombre":nombre, "Apellido":apellido}

    miHtml = open("C:/Users/maria/OneDrive/Documentos/Coder House - Python/Django Prueba 2/Prueba02/Proyecto02/Proyecto02/Plantillas/Template-1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
