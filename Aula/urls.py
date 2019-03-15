from django.urls import path, re_path
from Aula import views


urlpatterns = [
     path('', views.index),
     path('inicio-sesion/', views.inicio_sesion),
     path('inscripcion/', views.crear_estudiante, name = "inscripcion"),
     path('<int:carnet>', views.mostrar_datos_estudiante, name= 'datos_estudiante'),
     path('ver_estudiantes/', views.mostrar_estudiantes, name = 'estudiantes'),
     path('crear_curso/', views.crear_curso, name = 'crear-curso'),
     path('ver_cursos/', views.mostrar_cursos, name = 'cursos'),
]