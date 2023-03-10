from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppInicio.models import *
from AppInicio.forms import MyUserCreationForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

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

class DocentesCreate(LoginRequiredMixin, CreateView):
    model = Docente
    template_name = 'AppInicio/docentes-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'materia', 'mail', 'DNI']

class DocentesUpdate(LoginRequiredMixin, UpdateView):
    model = Docente
    template_name = 'AppInicio/docentes-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'materia', 'mail', 'DNI']

class DocentesDelete(LoginRequiredMixin, DeleteView):
    model = Docente
    template_name = 'AppInicio/docentes-eliminar.html'
    success_url = reverse_lazy('inicio')

# Views CRUD Alumnos:

class AlumnosLista(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'AppInicio/alumnos-list.html'

class AlumnosDetail(LoginRequiredMixin, DetailView):
    model = Alumno
    template_name ='AppInicio/alumnos-detalle.html'

class AlumnosCreate(LoginRequiredMixin, CreateView):
    model = Alumno
    template_name = 'AppInicio/alumnos-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'curso', 'mail', 'DNI', 'fecha_nacimiento']

class AlumnosUpdate(LoginRequiredMixin, UpdateView):
    model = Alumno
    template_name = 'AppInicio/alumnos-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'curso', 'mail', 'DNI', 'fecha_nacimiento']

class AlumnosDelete(LoginRequiredMixin, DeleteView):
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

class PracticasCreate(LoginRequiredMixin, CreateView):
    model = Practica
    template_name = 'AppInicio/practicas-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'materia', 'curso', 'fecha']

class PracticasUpdate(LoginRequiredMixin, UpdateView):
    model = Practica
    template_name = 'AppInicio/practicas-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'materia', 'curso', 'fecha']
    
class PracticasDelete(LoginRequiredMixin, DeleteView):
    model = Practica
    template_name = 'AppInicio/practicas-eliminar.html'
    success_url = reverse_lazy('inicio')

# Views para login

def login_request(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, 'AppInicio/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(request, 'AppInicio/login.html', {'mensaje': f'Hay un error! Los datos son incorrectos', 'form': form})
        else:
            return render(request, 'AppInicio/login.html', {'mensaje': f'Hay un error! Los datos son incorrectos', 'form': form})
    
    return render(request, 'AppInicio/login.html', {'form': form})

# View para registrar nuevo usuario:

def register(request):
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, 'AppInicio/inicio.html', {'mensaje': 'El usuario ha sido creado'})
        
    else:
        form = MyUserCreationForm()

    return render(request, 'AppInicio/registro.html', {'form': form})

