from django.shortcuts import render, redirect
from .models import Curso, Tareas #Importamos para hacer uso del modelo
from django.contrib import messages #Importamos para presentar mensajes
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            
            return render(request, 'signin.html', {"form": AuthenticationForm, "Error": "Username or password is incorrect."})

        login(request, user)
        return redirect('/atencion')
    
@login_required
def signout(request):
    logout(request)
    return redirect('/')
       
@login_required
def home(request):
    return redirect('/atencion') #cursos es como lo mandaré a llamar y definimos '' como cursos.html


def tareas(request):
    tareasListadas = Tareas.objects.all() #Pasamos a la variable lo que tiene el modelo
  #      cursosListados = Curso.objects.filter(creditos=1) Filter ayuda a hacer una clausula where
    messages.success(request, '¡Tareas listadas!') #Manda mensaje 
    return render(request, "cursos.html", {"tarea": tareasListadas}) #cursos es como lo mandaré a llamar y definimos '' como cursos.html

def registrarCurso(request):
    if request.method == 'POST':
            act = request.POST.get('txtAct')
            fecha = request.POST.get('dateFecha')
            nuevo_curso = Tareas.objects.create(txtAct=act, fecha=fecha)
            log_message = f"Usuario: {request.user.username}, Fecha: {datetime.now()}, Acción: Registro de Tarea ({act}) "
            with open("logs.txt", "a") as log_file:
             log_file.write(log_message + "\n")
            messages.success(request, "Se creó correctamente")
            return redirect('/atencion')

def edicionCurso(request, id):
    curso = Tareas.objects.get(id=id)
    curso.estado = 0
    curso.save()
    log_message = f"Usuario: {request.user.username}, Fecha: {datetime.now()}, Acción: Tarea ({curso.txtAct}) completada"
    with open("logs.txt", "a") as log_file:
        log_file.write(log_message + "\n")
    messages.success(request, "Completada con éxito")
    return redirect('/atencion')

def redirigirCurso(request, id):
    curso = Tareas.objects.get(id=id)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request, id):
    txtAct = request.POST['txtAct']
    fecha = request.POST['dateFecha']
    curso = Tareas.objects.get(id=id)
    curso.txtAct = txtAct
    curso.fecha = fecha
    curso.save()
    log_message = f"Usuario: {request.user.username}, Fecha: {datetime.now()}, Acción: Se editó la Tarea con id = {id} "
    with open("logs.txt", "a") as log_file:
        log_file.write(log_message + "\n")
    messages.success(request, '¡Tarea actualizada!')
    return redirect('/atencion')

def eliminarCurso(request, id):
    curso = Tareas.objects.get(id=id)
    curso.delete()
    log_message = f"Usuario: {request.user.username}, Fecha: {datetime.now()}, Acción: Tarea ({curso.txtAct}) eliminada"
    with open("logs.txt", "a") as log_file:
        log_file.write(log_message + "\n")
    messages.success(request, '¡Tarea eliminada!')
    return redirect('/atencion') #Indica a donde va a regresar






def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('/atencion')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
