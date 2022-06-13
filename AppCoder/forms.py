from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class EstudiantesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    

class EntregablesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    fechaDeEntrega= forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    entregado = forms.BooleanField()   
        
       