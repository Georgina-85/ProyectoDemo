from django.urls import path
from AppCoder import views




urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('curso/', views.curso, name='Curso'),
    path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'),
    #path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    #path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerProfesores/', views.leerProfesores, name='LeerProfesores'),
    path('eliminarProfesores/<nombre>', views.eliminarProfesores, name='EliminarProfesores'),
    path('editarProfesor/<profesor_nombre>', views.editarProfesor, name='EditarProfesor'),
    path('leerEstudiantes/', views.leerEstudiantes, name='LeerEstudiantes'),
    path('eliminarEstudiantes/<nombre>', views.eliminarEstudiantes, name='EliminarEstudiantes'),
     path('editarEstudiantes/<estudiante_nombre>', views.editarEstudiantes, name='EditarEstudiantes'),
  



]