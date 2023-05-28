from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<br><br><br>¡Hola mundo!<br><br>  ")