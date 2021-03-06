# Generated by Django 3.0.4 on 2020-03-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255, verbose_name='Nombres de Autor')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos de Autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('estado', models.BooleanField(default=True, verbose_name='Author Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoría')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada/No Activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
