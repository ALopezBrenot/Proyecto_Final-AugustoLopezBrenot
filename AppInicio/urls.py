# Archivo de URLS de la AppInicio

from django.urls import path
from AppInicio import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Inicio, name='inicio' ),
    # Urls del modelo Docente
    path('docentes-list/', DocentesLista.as_view(), name='docentes-list'),
    path('docentes-detalle/<pk>', DocentesDetail.as_view(), name='docentes-detalle'),
    path('docentes-nuevo/', DocentesCreate.as_view(), name='docentes-nuevo'),
    path('docentes-editar/<pk>', DocentesUpdate.as_view(), name='docentes-editar'),
    path('docentes-eliminar/<pk>', DocentesDelete.as_view(), name='docentes-eliminar'),

    # Urls del modelo Alumnos
    path('alumnos-list/', AlumnosLista.as_view(), name='alumnos-list'),
    path('alumnos-detalle/<pk>', AlumnosDetail.as_view(), name='alumnos-detalle'),
    path('alumnos-nuevo/', AlumnosCreate.as_view(), name='alumnos-nuevo'),
    path('alumnos-editar/<pk>', AlumnosUpdate.as_view(), name='alumnos-editar'),
    path('alumnos-eliminar/<pk>', AlumnosDelete.as_view(), name='alumnos-eliminar'),

    # Urls del modelo Prácticas
    path('practicas-list/', PracticasLista.as_view(), name='practicas-list'),
    path('practicas-detalle/<pk>', PracticasDetail.as_view(), name='practicas-detalle'),
    path('practicas-nuevo/', PracticasCreate.as_view(), name='practicas-nuevo'),
    path('practicas-editar/<pk>', PracticasUpdate.as_view(), name='practicas-editar'),
    path('practicas-eliminar/<pk>', PracticasDelete.as_view(), name='practicas-eliminar'),

    #Path para Login / Logout
    path('login/', views.login_request, name='login'),
    path('registro/', views.register, name='registrar'),
    path('logout/', LogoutView.as_view(template_name= 'AppInicio/logout.html'), name='logout')

]