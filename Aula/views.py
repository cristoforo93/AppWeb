from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Estudiante, EstudianteForm, CursoForm, Curso
from django.urls import reverse
# Create your views here.

def index(request):
    template =  loader.get_template('Aula/base.html')
    context = {}
    return HttpResponse(template.render(context,request))


def inicio_sesion(request):
    template =  loader.get_template('Aula/inicio-sesion.html')
    context = {'nombre_usuario': 'Cristian Gay'}
    return HttpResponse(template.render(context,request))


def mostrar_estudiantes(request):
    lista = Estudiante.objects.order_by('-numero_carnet')
    contexto = {'inscritos': lista}
    template = loader.get_template('Aula/listar-estudiantes.html')
    return  render(request, 'Aula/listar-estudiantes.html', contexto)

def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nuevo_estudiante = form.save(commit = False)
            print(nuevo_estudiante)
            nuevo_estudiante.save()
            return HttpResponseRedirect( reverse('datos_estudiante', kwargs= {'carnet':nuevo_estudiante.numero_carnet} ) )
    else:
        form = EstudianteForm()

    return render(request, 'Aula/crear-usuario.html',{'formulario':form})


def crear_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return HttpResponseRedirect( reverse('cursos') )
    else:
        form = CursoForm()

    return render(request, 'Aula/crear-curso.html', {'formulario':form})


def mostrar_datos_estudiante(request, carnet):
    estudiante = Estudiante.objects.get(pk=carnet)
    context = {'nombre': estudiante.nombres , 'apellido': estudiante.apellidos,
               'carnet': carnet , 'carrera': estudiante.carrera }

    template = loader.get_template('Aula/datos-estudiante.html')
    return  HttpResponse(template.render(context, request))


def mostrar_cursos(request):
    lista_cursos = Curso.objects.order_by('codigo_curso')
    contexto = {'cursos':lista_cursos}
    template = loader.get_template('Aula/listar-cursos.html')
    return HttpResponse(template.render(contexto, request))
