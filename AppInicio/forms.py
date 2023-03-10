# Archivo de formularios de AppInicio

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario:', widget= forms.TextInput)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña:', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña:', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k: '' for k in fields}