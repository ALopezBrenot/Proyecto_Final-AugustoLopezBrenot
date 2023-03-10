# Proyecto_Final-AugustoLopezBrenot
Repositorio del proyecto final de Python para CoderHouse

# Instrucciones para clonar el repositorio y setear el proyecto 馃捇

## Es necesario crear una carpeta donde se va a clonar el repositorio.

Utilizando Git bash, solicitar la clonaci贸n del repositorio:

```
# git clone + https://github.com/ALopezBrenot/Proyecto_Final-AugustoLopezBrenot.git
```

Cambiar la ruta a la carpeta creada tras la clonaci贸n:

```
> cd + nombre de la carpeta
```

En la carpeta del proyecto, instalar y crear el entorno virtual:

```
> pip install virtualenv

> python -m venv venv
```

Activar el entorno virtual:

```
> venv\Scripts\activate
```
Instalar Django en el entorno virtual:

```
> pip install django
```

En el repositorio existe un archivo con las dependencias que es necesario instalar para correr el proyecto adecuadamente, el mismo puede ser leido e instalado de la siguiente manera:

```
pip install -r requirements.txt
```

El proyecto cuenta con una BBDD, para utilizarlo se deben realizar las migraciones correspondientes:

```
python manage.py migrate
```

Correr el servidor local, que permitir谩 visualizar las vistas:

```
python manage.py runserver
```

Se recomienda crear un super-usuario para poder gestionar todos los archivos:

```
python manage.py createsuperuser
```

La p谩gina es un blog de laboratorio escolar que puede almacenar informaci贸n de Docentes, Alumnos y clases Pr谩cticas dictadas. Adem谩s permite a los usuarios generar posteos en la secci贸n correspondiente. Es necesario crear un usuario e iniciar sesi贸n para poder acceder las opciones de edici贸n o eliminaci贸n de cada una de las categor铆as.

Video de muestra de las funcionalidades:
