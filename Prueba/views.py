from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def primera_pagina(request):
    return HttpResponse("Hola Mundo")

def segunda_pagina(request):
    return HttpResponse("Adios Adriana")

def tercera_pagina(request):
    return HttpResponse("Que bueno que volviste Adriana")
