# Archivo de URLS de la AppPosts

from django.urls import path
from .views import *

urlpatterns = [
    path('post-list/', PostsLista.as_view(), name='post-list'),
    path('detalle/<pk>', PostsDetalle.as_view(), name='detalle'),
    path('nuevo/', PostsCreacion.as_view(), name='nuevo'),
    path('editar/<pk>', PostsUpdate.as_view(), name='editar'),
    path('eliminar/<pk>', PostsDelete.as_view(), name='eliminar'),
    ]