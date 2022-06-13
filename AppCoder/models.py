from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cursos"
        verbose_name = "Curso"

    def __str__(self): 
        return f"{self.nombre} {self.camada}"


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)  
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Estudiantes"
        verbose_name = "Estudiante"

    def __str__(self): 
        return f"{self.nombre}  {self.apellido} - {self.email}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)  
    apellido = models.CharField(max_length=40)
    email = models.EmailField()   
    profesion = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Profesores"
        verbose_name = "Profesor"

    def __str__(self): 
        return f"{self.nombre}  {self.apellido} - {self.email} - {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField() 
    entregado = models.BooleanField()   

    class Meta:
        verbose_name_plural = "Entregables"
        verbose_name = "Entregable"

    def __str__(self): 
        return f"{self.nombre} - {self.fechaDeEntrega}"