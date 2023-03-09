# Archivo de URLS de la AppInicio

from django.urls import path
from AppInicio import views
from .views import *

urlpatterns = [
    path('', views.Inicio, name='inicio' ),
    # Urls del modelo Docente
    path('docentes-list/', DocentesLista.as_view(), name='docentes-list'),
    path('docentes-detalle/<pk>', DocentesDetail.as_view(), name='docentes-detalle'),
    path('docentes-nuevo/', DocentesCreate.as_view(), name='docentes-nuevo'),
    path('docentes-editar/<pk>', DocentesUpdate.as_view(), name='docentes-editar'),
    path('docentes-eliminar/<pk>', DocentesDelete.as_view(), name='docentes-eliminar'),
    
]