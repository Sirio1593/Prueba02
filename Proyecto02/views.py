from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime as dt

def saludo(request):
    return HttpResponse("<br><br><br>¡Hola mundo!<br><br>  ")

def dia(request):
    dia = dt.datetime.now()
    return HttpResponse(f"<br><br><br>La fecha y hora de hoy es {dia}<br><br>  ")

def template1(self):
    nombre = "Mariano"
    apellido = "Sirio"
    notas = [1,2,3,4,5,6,7,8,9]
    diccionario = {"Nombre":nombre, "Apellido":apellido, "Ahora":str(dt.now()),"Notas":notas}
    
    plantilla = loader.get_template('Template-1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)