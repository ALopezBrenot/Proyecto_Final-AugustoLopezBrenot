from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppInicio.models import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.

# Vista inicio
def Inicio (request):
    return render(request, 'AppInicio/inicio.html')


# Views CRUD Docentes: (Vistas basadas en clases)

class DocentesLista(ListView):
    model = Docente
    template_name = 'AppInicio/docentes-list.html'

class DocentesDetail(DetailView):
    model = Docente
    template_name ='AppInicio/docentes-detalle.html'

class DocentesCreate(CreateView):
    model = Docente
    template_name = 'AppInicio/docentes-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'materia', 'mail', 'DNI']

class DocentesUpdate(UpdateView):
    model = Docente
    template_name = 'AppInicio/docentes-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'materia', 'mail', 'DNI']

class DocentesDelete(DeleteView):
    model = Docente
    template_name = 'AppInicio/docentes-eliminar.html'
    success_url = reverse_lazy('inicio')

# Views CRUD Alumnos:

class AlumnosLista(ListView):
    model = Alumno
    template_name = 'AppInicio/alumnos-list.html'

class AlumnosDetail(DetailView):
    model = Alumno
    template_name ='AppInicio/alumnos-detalle.html'

class AlumnosCreate(CreateView):
    model = Alumno
    template_name = 'AppInicio/alumnos-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'curso', 'mail', 'DNI', 'fecha_nacimiento']

class AlumnosUpdate(UpdateView):
    model = Alumno
    template_name = 'AppInicio/alumnos-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'curso', 'mail', 'DNI', 'fecha_nacimiento']

class AlumnosDelete(DeleteView):
    model = Alumno
    template_name = 'AppInicio/alumnos-eliminar.html'
    success_url = reverse_lazy('inicio')

# Views CRUD Práctica

class PracticasLista(ListView):
    model = Practica
    template_name = 'AppInicio/practicas-list.html'

class PracticasDetail(DetailView):
    model = Practica
    template_name ='AppInicio/practicas-detalle.html'

class PracticasCreate(CreateView):
    model = Practica
    template_name = 'AppInicio/practicas-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'materia', 'curso', 'fecha']

class PracticasUpdate(UpdateView):
    model = Practica
    template_name = 'AppInicio/practicas-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'materia', 'curso', 'fecha']
    
class PracticasDelete(DeleteView):
    model = Practica
    template_name = 'AppInicio/practicas-eliminar.html'
    success_url = reverse_lazy('inicio')