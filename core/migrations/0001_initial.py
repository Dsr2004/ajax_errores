# Generated by Django 3.2.9 on 2022-02-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='frutas',
            fields=[
                ('id_fruta', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id de la Fruta')),
                ('nombre', models.CharField(max_length=40, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
    ]
