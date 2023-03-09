# Generated by Django 4.1.7 on 2023-03-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('curso', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('DNI', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('materia', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('DNI', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Practica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('materia', models.CharField(max_length=30)),
                ('curso', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]
