from django.db import models

class Mascota(models.Model):
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    edad=models.IntegerField(verbose_name="Edad")
    especie=models.CharField(max_length=100, verbose_name="Especie")
    tamaño=models.CharField(max_length=100, verbose_name="Tamaño")
    tipo=models.CharField(max_length=100, verbose_name="Tipo")
    manto=models.CharField(max_length=100, verbose_name="Manto")
    castracion=models.CharField(max_length=10, verbose_name="Castracion")
    #def __str__(self):
    #    return f"{self.nombre} | {self.especie} | Años:{self.edad}"
    def __str__(self):
        return self.nombre

class Refugio(models.Model):
    sala1=models.CharField(max_length=100, verbose_name="Sala 1")
    sala2=models.CharField(max_length=100, verbose_name="Sala 2")
    sala3=models.CharField(max_length=100, verbose_name="Sala 3")
    sala4=models.CharField(max_length=100, verbose_name="Sala 4")
    mascotas=models.ManyToManyField(Mascota)

class Persona(models.Model):
    nombre=models.CharField(max_length=200, verbose_name="Nombre")
    apellido=models.CharField(max_length=200, verbose_name="Apellido")
    #DNI unique para que sólo se postule una vez!!
    dni=models.IntegerField(verbose_name="DNI", unique=True,null=True)
    telefono=models.IntegerField(verbose_name="Telefono")
    
    class Meta:
        abstract=True
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Colaborador(Persona):
    cuit=models.IntegerField(verbose_name="CUIT", unique=True,null=True)
    turno=models.CharField(max_length=100, verbose_name="Turno")
    def __str__(self):
        return f"{self.nombre_completo()} | DNI:{self.dni}| {self.turno}"
    
class Postulante(Persona):
    calle=models.CharField(max_length=100, verbose_name="Calle")
    numero=models.IntegerField(verbose_name="Número")
    localidad=models.CharField(max_length=100, verbose_name="Localidad")
    vivienda=models.CharField(max_length=100, verbose_name="Vivienda")
    tieneMascota=models.CharField(max_length=10, verbose_name="Tiene Mascota")   
    motivo=models.CharField(max_length=200, verbose_name="Motivo")
    #mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE, null=True, blank=True) 
    #Este campo es de realación uno a muchos! 
    #Mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)
    #def __str__(self):
     #   return f"{self.nombre} {self.apellido} | DNI:{self.dni}"
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Adopcion(models.Model):
    #nombre = models.CharField(max_length=100, verbose_name="Nombre")
    #descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    #fecha_entrevista = models.DateField(verbose_name="Fecha de entrevista")
    postulacion=models.ForeignKey(Postulante, on_delete=models.CASCADE)
    adopcion=models.ForeignKey(Mascota, on_delete=models.CASCADE)
    #fecha_Adopcion= models.DateField(verbose_name="Fecha de Adopción",auto_now_add=True)
    fecha_entrevista = models.DateField(verbose_name="Fecha de Entrevista")
    #def __str__(self):
    #    return f"{self.postulacion} | {self.adopcion} | Fecha Entrevista:{self.fecha_entrevista}"
    #Mascota=models.OneToOneField (Mascota on_delete=models.CASCADE, primary_key=true) 
#  Create your models here.
    def __str__(self):
        return f"Adopción de {self.mascota} por {self.postulante} el {self.fecha_adopcion}"
    
"""
    refugio
sala 1 mascotas
sala 2 mascotas
sala 3 mascotas
sala 4 mascotas

    Mascota
nombre
edad 
especie
tamaño
tipo 
manto
sala
   
    Persona:
nombre
apellido 
dni
telefono

   Colaborador(persona)
#nombre
#apellido 
#dni
#telefono
Turno

    Postulante(persona)
#nombre
#apellido 
#dni
#telefono
calle
localidad
vivienda
tieneMascota
motivo 

   Adopcion
postulacion
adopcion
fecha_Adopcion  
"""
#Relaciones
"""
n a n --> Muchas Mascotas en Muchas salas
1 a N -->Mascota puede tener varios Postulantes
1 a 1 -->una MAscota tiene una adopción
1 a n --> un adoptante puede adoptar 2 mascotas

"""