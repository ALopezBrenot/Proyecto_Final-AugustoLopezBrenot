from django.db import models

# Create your models here.

class Post(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()
    usuario = models.CharField(max_length=40)
    contenido = models.CharField(max_length=300)