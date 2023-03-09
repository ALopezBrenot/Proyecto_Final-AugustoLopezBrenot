# Archivo de URLS de la AppInicio

from django.urls import path
from AppInicio import views

urlpatterns = [
    path('', views.Inicio, name='inicio' ),
    path('docentes/', views.Docentes, name='docentes'),
    path('alumnos/', views.Alumnos, name='alumnos'),
    path('practicas/', views.Practicas, name='practicas'),
    path('busqueda-clase/', views.busqueda_clase, name='busqueda-clase'),
    path('buscar/', views.buscar, name='buscar')
]