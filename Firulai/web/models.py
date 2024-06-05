from django.db import models

class Mascota(models.Model):
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    edad=models.IntegerField(verbose_name="Edad")
    especie=models.CharField(max_length=100, verbose_name="Especie")
    tamaño=models.CharField(max_length=100, verbose_name="Tamaño")
    tipo=models.CharField(max_length=100, verbose_name="Tipo")
    manto=models.CharField(max_length=100, verbose_name="Manto")

class Postulante(models.Model):
    nombre=models.CharField(max_length=200, verbose_name="Nombre")
    apellido=models.CharField(max_length=200, verbose_name="Apellido")
    dni=models.IntegerField(verbose_name="DNI")
    telefono=models.IntegerField(verbose_name="Telefono")
    calle=models.CharField(max_length=100, verbose_name="Calle")
    numero=models.IntegerField(verbose_name="Número")
    localidad=models.CharField(max_length=100, verbose_name="Localidad")
    vivienda=models.CharField(max_length=100, verbose_name="Vivienda")
    tieneMascota=models.CharField(max_length=10, verbose_name="Tiene Mascota")
    motivo=models.CharField(max_length=200, verbose_name="Motivo")

class Adopcion(models.Model):
    postulacion=models.ForeignKey(Postulante, on_delete=models.CASCADE)
    adopcion=models.ForeignKey(Mascota, on_delete=models.CASCADE)

# Create your models here.
