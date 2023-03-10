# Proyecto_Final-AugustoLopezBrenot
Repositorio del proyecto final de Python para CoderHouse

# Instrucciones para clonar el repositorio y setear el proyecto 💻

## Es necesario crear una carpeta donde se va a clonar el repositorio.

Utilizando Git bash, solicitar la clonación del repositorio:

```
# git clone + https://github.com/ALopezBrenot/Proyecto_Final-AugustoLopezBrenot.git
```

Cambiar la ruta a la carpeta creada tras la clonación:

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

Correr el servidor local, que permitirá visualizar las vistas:

```
python manage.py runserver
```

Se recomienda crear un super-usuario para poder gestionar todos los archivos:

```
python manage.py createsuperuser
```

La página es un blog de laboratorio escolar que puede almacenar información de Docentes, Alumnos y clases Prácticas dictadas. Además permite a los usuarios generar posteos en la sección correspondiente. Es necesario crear un usuario e iniciar sesión para poder acceder las opciones de edición o eliminación de cada una de las categorías.

Video de muestra de las funcionalidades:
