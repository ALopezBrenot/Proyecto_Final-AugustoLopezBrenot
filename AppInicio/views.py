from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppInicio.models import *
from AppInicio.forms import MyUserCreationForm, UserEditForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

# Vista para editar perfiles

@login_required
def editar_perfil(request):
    usuario = User.objects.get(username=request.user)

    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            return redirect('/')
         

    else:
        mi_formulario = UserEditForm(initial={'username': usuario.username,
                                     'email': usuario.email,
                                     'last_name': usuario.last_name,
                                     'first_name': usuario.first_name})
        
    return render(request, 'AppInicio/editar-perfil.html', {'mi_formulario': mi_formulario, 'usuario':usuario})

# Vista para cambiar avatar

@login_required
def agregar_avatar(request):
    avatar = request.user.avatar
    mi_formulario = AvatarFormulario(instance=avatar)

    if request.method == 'POST':
        mi_formulario = AvatarFormulario(request.POST, request.FILES, instance=avatar)
        if mi_formulario.is_valid():
            mi_formulario.save()

            return redirect('/')
    
    else:
        return render(request, 'AppInicio/agregar-avatar.html', {'mi_formulario': mi_formulario})
    

