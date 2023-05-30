from django.shortcuts import render
from AppProyecto02.models import Persona

# Create your views here.

nuevaPesona = Persona(nombre="Mariano", apellido="Sirio", dirección="Lucero 1068")
Persona.save()

