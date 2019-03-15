from django.db import models
from django.forms import ModelForm
# Create your models here.

class Estudiante(models.Model):
    numero_carnet = models.CharField(max_length=10, primary_key = True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)

    def __unicode__(self):
        return self.numero_carnet

class EstudianteForm(ModelForm):

    class Meta:
        model = Estudiante
        fields = ["numero_carnet", "nombres", "apellidos", "carrera"]


class Curso(models.Model):
    codigo_curso = models.CharField(max_length=5, primary_key = True)
    nombre_curso = models.CharField(max_length=40)
    creditos = models.IntegerField()

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo_curso', 'nombre_curso', 'creditos']

class Asignacion(models.Model):
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)



