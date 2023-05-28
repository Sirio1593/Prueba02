import datetime as dt
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<br><br><br>¡Hola mundo!<br><br>  ")

def dia(request):
    dia = dt.datetime.now()
    return HttpResponse(f"<br><br><br>La fecha y hora de hoy es {dia}<br><br>  ")