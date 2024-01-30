from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('atencion', views.tareas, name="tareas"),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<id>', views.edicionCurso),
    path('editarCurso/<id>', views.redirigirCurso),
    path('eliminarCurso/<id>', views.eliminarCurso),
    path('modificar/<id>', views.editarCurso),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
  
  #   path('pruebaCurso/<codigo>', views.pruebaCurso)
]