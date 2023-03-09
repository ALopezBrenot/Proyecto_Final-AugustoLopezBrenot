from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppInicio.models import *

# Create your views here.

# Vista inicio
def Inicio (request):
    return render(request, 'AppInicio/inicio.html')

# Vistas para la búsqueda de clases en la página de inicio

def busqueda_clase(request):
    return render(request, 'AppInicio/inicio.html')

def buscar(request):
    if request.GET['fecha']:
        mi_fecha = request.GET['fecha']
        resultado = Practica.objects.filter(fecha__icontains = mi_fecha)

        return render(request, 'AppInicio/inicio.html', {'clase':resultado , 'fecha': mi_fecha})
    
    else:
        respuesta = 'No se encontraron clases en esa fecha'

    return HttpResponse (respuesta)

# Views de las demás categorías
def Docentes(request):
    return render(request,'AppInicio/docentes.html')

def Alumnos(request):
    return render(request,'AppInicio/alumnos.html')

def Practicas(request):
    return render(request,'AppInicio/practicas.html')