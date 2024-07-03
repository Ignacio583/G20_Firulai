from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import *
from .models import Postulante, Colaborador, Adopcion, Mascota
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#Index ?

def index (request):
    context= {
        'fecha_hora':datetime.datetime.now()
    }
    return render (request,"web/index.html",context)

#Logins
def user_logout(request):
    logout(request)

    messages.success(request, 'Sesion Cerrada')

    return redirect('index')

#Acerca del Refugio

def refugio (request):
    contexto ={}
    return render (request, 'web/refugio.html', contexto)

@login_required
def alta_postulante(request):
    contexto={}
    if request.method == "GET":
        contexto['alta_postulante']= AdopcionFormulario()
    else: #asumo que es un POST y me crea un diccionario con 
        #los datos que el usuario ingreso en el formulario
        form = AdopcionFormulario(request.POST)
        contexto['alta_postulante']= form
        
        if form.is_valid():
            #Si el form es correcto lo redirijo a una vista segura como por ejemplo el index
            #falta la clase postulante!!!!!
            nuevo_postulante=AdopcionFormulario(
                nombre= form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                dni=form.cleaned_data['DNI'],
                calle=form.cleaned_data['calle'],
                localidad=form.cleaned_data['localidad'],
            )         
            nuevo_postulante.save()
                
            messages.success(request, 'El Formulario fue incorporado con éxito')
            
        #Si el FORM es correcto, lo redirijo a una vista segura, como el index, para que no se vuelva a completar el formulario.
            return redirect('index') #el return debe ir cerrando el ciclo y en este caso cerrando el segundo if
    print(request.POST )
    return render(request, 'web/alta_postulante.html', contexto)

#Alta de Postulante 

"""def alta_postulante(request):
    contexto={}
    if request.method == "GET":
        contexto['alta_postulante']= alta_adopcion()
    else: #asumo que es un POST y me crea un diccionario con 
        #los datos que el usuario ingreso en el formulario
        form = alta_adopcion(request.POST)
        contexto['alta_postulante']= form
        
        if form.is_valid():
            #Si el form es correcto lo redirijo a una vista segura como por ejemplo el index
            #falta la clase postulante!!!!!
            nuevo_postulante=alta_adopcion(
                nombre= form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                dni=form.cleaned_data['DNI'],
                calle=form.cleaned_data['calle'],
                localidad=form.cleaned_data['localidad'],
            )         
            nuevo_postulante.save()
                
            messages.success(request, 'El postulante fue dado de alta sin problemas')
            
        #Si el FORM es correcto, lo redirijo a una vista segura, como el index, para que no se vuelva a completar el formulario.
            return redirect('index') #el return debe ir cerrando el ciclo y en este caso cerrando el segundo if
    print(request.POST )
    return render(request, 'web/alta_postulante.html', contexto)"""

#Alta de Mascotas

def alta_mascota(request):
    contexto={}
    if request.method == "GET":
        contexto['alta_mascota_form']= MascotaFormulario()
    else: #asumo que es un POST y me crea un diccionario con los datos que el usuario ingreso en el formulario
        form = MascotaFormulario(request.POST)
        contexto['alta_mascota_form']= form
        #validamos el form
        if form.is_valid():
            #Si el form es correcto lo redirijo a una vista segura como por ejemplo el index
            nueva_mascota=Mascota(
                nombre=form.cleaned_data['nombre'],
                edad=form.cleaned_data['edad'],
                especie=form.cleaned_data['especie'],
                tamaño=form.cleaned_data['tamaño'],
                tipo=form.cleaned_data['tipo'],
                manto=form.cleaned_data['manto'],
                castracion=form.cleaned_data['castracion'],
            )
            nueva_mascota.save()
            messages.success(request, 'La Mascota fue ingresada con éxito')
        #Si el FORM es correcto, lo redirijo a una vista segura, como el index, para que no se vuelva a completar el formulario.
            return redirect('index') #el return debe ir cerrando el ciclo y en este caso cerrando el segundo if
    print(request.POST )
    return render(request, 'web/alta_mascota.html', contexto)

#Formulario de Adopcion Model Forms
def alta_adopcion(request):
    contexto = {}
    if request.method == "GET":
        formulario = AdopcionFormulario()
    else:
        formulario = AdopcionFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'La adopcion fue registrada con exito, pendiente de aprobacion')
            return redirect('index')
    contexto["formulario"] = formulario
    return render(request, 'web/alta_adopcion.html', contexto)

#Formulario Postulante Model Form
def alta_postulante(request):
    contexto = {}
    if request.method == "GET":
        formulario = PostulanteFormulario() #esta variable formulario es la que voy a llamar en el HTML , el alta_postulante me llama al vinculo del URL y el formulario me lleva el formulario!!!!!!!!!!!!!
    else:
        formulario = PostulanteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'El Postulante se registró exitosamente.')
            return redirect ('index')
    contexto["formulario"]=formulario 
    return render(request, 'web/alta_postulante.html', contexto)


#Vista vasada en Clases
#Postulantes

class PostulanteListView(ListView):
    model= Postulante
    context_object_name='Postulante'
    template_name='web/listado_postulante.html'
    ordering = ['dni']

#Colaboradores

class ColaboradorListView(ListView):
    model= Colaborador
    context_object_name='Colaborador'
    template_name='web/listado_colaborador.html'
    ordering = ['turno']

#Adopciones

class AdopcionesLista(ListView):
    model= Adopcion
    context_object_name='Adopcion'
    template_name='web/listado_adopciones.html'
    ordering = ['adopciones']
    def get_queryset(self):
        return Adopcion.objects.select_related('postulacion', 'adopcion')
