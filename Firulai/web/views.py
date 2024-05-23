from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index (request):
    context= {
        'fecha_hora':datetime.datetime.now()
    }
    return render (request,"web/index.html",context)

def Refugio_1 (request):
    contexto ={}
    return render (request, 'web/Refugio_1.html', contexto)

def FormularioAdop (request):
    formulario = {}
    return render (request, 'web/FormularioAdop.html', formulario)