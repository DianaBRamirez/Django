from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('atencion', views.homes),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<id>', views.eliminarCurso)
  #   path('pruebaCurso/<codigo>', views.pruebaCurso)
]