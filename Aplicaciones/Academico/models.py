from django.db import models

# Create your models here.


class Curso(models.Model):
    id = models.AutoField(primary_key=True) #Es una prueba de un id autoincrementable
  
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

 
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    
  #  def total(self):
  #       return (self.creditos * self.creditos)