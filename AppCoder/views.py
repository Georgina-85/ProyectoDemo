from django.http import HttpResponse 
from django.shortcuts import render, HttpResponse
from django.template import loader
from AppCoder.models import Curso, Profesor, Estudiantes, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudiantesFormulario, EntregablesFormulario
from django.views.generic import ListView


# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")
    

def curso(request):
    return render(request, "AppCoder/curso.html")

    
def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def curso(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre= informacion['curso']
            camada= informacion['camada']
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()        
        
    return render(request, "AppCoder/curso.html", {"miFormulario":miFormulario})    

def profesores(request):
  if request.method == 'POST':
    miFormulario = ProfesorFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    apellido = informacion['apellido']
    email = informacion['email']
    profesion = informacion['profesion']

    profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    profesor.save()
    return render(request, "AppCoder/inicio.html")
  else:
    miFormulario = ProfesorFormulario()
  return render(request, 'appCoder/profesores.html', {'miFormulario':miFormulario})

def estudiantes(request):
  if request.method == 'POST':
    miFormulario = EstudiantesFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    apellido = informacion['apellido']
    email = informacion['email']
    

    estudiantes = Estudiantes(nombre=nombre, apellido=apellido, email=email)
    estudiantes.save()
    return render(request, "AppCoder/inicio.html")
  else:
    miFormulario = EstudiantesFormulario()
  return render(request, 'appCoder/estudiantes.html', {'miFormulario':miFormulario})  

def entregables(request):
  if request.method == 'POST':
    miFormulario = EntregablesFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    fechaDeEntrega= informacion['fechaDeEntrega']
    entregado = informacion['entregado']
 

    entregables = Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entregado=entregado)
    entregables.save()
    return render(request, "AppCoder/inicio.html")
  else:
    miFormulario = EntregablesFormulario()
  return render(request, 'appCoder/entregables.html', {'miFormulario':miFormulario})  


def buscar(request):

  if  request.GET["camada"]:

	  #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
    camada = request.GET['camada'] 
    cursos = Curso.objects.filter(camada__icontains=camada)

    return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

  else: 

	  respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
  return HttpResponse(respuesta)


def leerProfesores(request):
  profesores = Profesor.objects.all() #trae todos los profesores
  contexto = {"profesores": profesores}
  return render(request, "AppCoder/leerProfesores.html", contexto)

def eliminarProfesores(request, nombre):
  profesor = Profesor.objects.get(nombre=nombre)
  profesor.delete()

  #vuelvo al menu

  profesores = Profesor.objects.all()
  contexto = {"profesores": profesores}
  return render(request, "AppCoder/leerProfesores.html", contexto) 

def editarProfesor(request, profesor_nombre):
  profesor = Profesor.objects.get(nombre=profesor_nombre)
  if request.method == 'POST':
    miFormulario = ProfesorFormulario(request.POST)

    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
      profesor.nombre = informacion['nombre']
      profesor.apellido = informacion['apellido']
      profesor.email = informacion['email']
      profesor.profesion = informacion['profesion']
      profesor.save()

      return render(request, 'appCoder/inicio.html')
  else:
    miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion}) 
    
    return render(request, 'appCoder/editarProfesor.html', {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})


def leerEstudiantes(request):
  estudiantes = Estudiantes.objects.all() #trae todos los estudiantes
  contexto = {"estudiantes": estudiantes}
  return render(request, "AppCoder/leerEstudiantes.html", contexto)

def eliminarEstudiantes(request, nombre):
  estudiantes = Estudiantes.objects.get(nombre=nombre)
  estudiantes.delete()

  #vuelvo al menu

  estudiantes = Estudiantes.objects.all()
  contexto = {"estudiantes": estudiantes}
  return render(request, "AppCoder/leerEstudiantes.html", contexto) 

def editarEstudiantes(request, estudiante_nombre):
  estudiantes = Estudiantes.objects.get(nombre=estudiante_nombre)
  if request.method == 'POST':
    miFormulario = EstudiantesFormulario(request.POST)

    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
      estudiantes.nombre = informacion['nombre']
      estudiantes.apellido = informacion['apellido']
      estudiantes.email = informacion['email']
      
      estudiantes.save()

      return render(request, 'appCoder/inicio.html')
  else:
    miFormulario = EstudiantesFormulario(initial={'nombre':estudiantes.nombre, 'apellido':estudiantes.apellido, 'email':estudiantes.email,}) 
    
    return render(request, 'appCoder/editarEstudiantes.html', {"miFormulario": miFormulario, "estudiante_nombre": estudiante_nombre})










#LISTVIEW ------------------------------------
class CursoList(ListView):
  model = Curso
  template_name = "AppCoder/curso.html"
