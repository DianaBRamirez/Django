from django.shortcuts import render, redirect
from .models import Curso #Importamos para hacer uso del modelo
from django.contrib import messages #Importamos para presentar mensajes

# Create your views here.



def home(request):
    return render(request, "ho.html") #cursos es como lo mandaré a llamar y definimos '' como cursos.html

def homes(request):
    cursosListados = Curso.objects.all() #Pasamos a la variable lo que tiene el modelo
  #      cursosListados = Curso.objects.filter(creditos=1) Filter ayuda a hacer una clausula where
    messages.success(request, '¡Cursos listados!') #Manda mensaje 
    return render(request, "cursos.html", {"cursos": cursosListados}) #cursos es como lo mandaré a llamar y definimos '' como cursos.html



def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/atencion')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/atencion')




def eliminarCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/atencion') #Indica a donde va a regresar

#def pruebaCurso(request,codigo):     cambiar un sólo dato
 #   nombre = "hola"

   # curso = Curso.objects.get(codigo=codigo)
   # curso.nombre = nombre
   # curso.save()

   # messages.success(request, '¡Nombre actualizado!')

   # return redirect('/atencion')