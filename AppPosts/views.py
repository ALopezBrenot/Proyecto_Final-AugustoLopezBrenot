#Archivo de vistas de la AppPosts

from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppPosts.models import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.

class PostsLista(ListView):
    model = Post
    template_name = 'AppPosts/posts-list.html'

class PostsDetalle(DetailView):
    model = Post
    template_name = 'AppPosts/posts-detalle.html'

class PostsCreacion(CreateView):
    model = Post
    template_name = 'AppPosts/posts-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'fecha', 'usuario', 'contenido']

class PostsUpdate(UpdateView):
    model = Post
    template_name = 'AppPosts/posts-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'fecha', 'usuario', 'contenido']

class PostsDelete(DeleteView):
    model = Post
    template_name = 'AppPosts/posts-eliminar.html'
    success_url = reverse_lazy('inicio')