from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages

def index (request):
    context= {
        'fecha_hora':datetime.datetime.now()
    }
    return render (request,"web/index.html",context)

def Refugio_1 (request):
    contexto ={}
    return render (request, 'web/Refugio_1.html', contexto)

def alta_postulante(request):
    contexto={}
    if request.method == "GET":
        contexto['FormularioAdop']= FormularioAdop()
    else: #asumo que es un POST y me crea un diccionario con los datos que el usuario ingreso en el formulario
        form = FormularioAdop(request.POST)
        contexto['FormularioAdop']= form
        #validamos el form
        if form.is_valid():
            #Si el form es correcto lo redirijo a una vista segura como por ejemplo el index
            messages.success(request, 'El alumno fue dado de alta con éxito')
        #Si el FORM es correcto, lo redirijo a una vista segura, como el index, para que no se vuelva a completar el formulario.
            return redirect('index') #el return debe ir cerrando el ciclo y en este caso cerrando el segundo if
    print(request.POST )
    return render(request, 'web/FormularioAdop.html', contexto)


def Contacto (request):
    formulario = {}
    return render (request, 'web/Contacto.html', formulario)