from django import forms
from django.core.exceptions import ValidationError
from .models import Adopcion, Postulante

#Adoptates

class PostulanteFormulario(forms.ModelForm):
    class Meta:
        model = Postulante
        fields = '__all__'

        error_messages = {
            'dni' : {
                'required' : 'El Campo DNI es Obligatorio'
            }
        }
    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El Nombre solo puede estar compuesto por letras")
        return self.cleaned_data["nombre"]
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El Apellido solo debe estar compuesto por letras")
        return self.cleaned_data["apellido"]



"""class  Postulante(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=20, required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'})) 
    apellido = forms.CharField(label="Apellido", max_length=20, required=True) 
    dni = forms.IntegerField(label="DNI", required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)
    calle = forms.CharField(label="calle", max_length=20, required=True)
    numero = forms.IntegerField(label="Número", required=True)
    localidad = forms.CharField(label="Localidad", max_length=20, required=True)
    vivienda = forms.ChoiceField(label="Vivienda", required=True, choices=viviendas)
    tieneMascota = forms.BooleanField(label="Ya tiene Mascota", required=True)
    motivo = forms.CharField(label="Especifique brevemente los motivos por el cual desea adoptar una mascota", max_length=200, required=True)

    #direccion = forms.CharField(label="Direccion", required=True)

    #CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    #field = forms.ChoiceField(choices=CHOICES)

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")

        return self.cleaned_data["apellido"]
    
    def clean_dni(self):
        if not self.cleaned_data["DNI"].isdigit():
            raise ValidationError("El DNI solo puede estar compuesto por númeor")

        return self.cleaned_data["DNI"]
    
    def clean_calle(self):
        if not self.cleaned_data["calle"].isalpha():
            raise ValidationError("El nombre de la calle solo puede estar compuesto por letras")

        return self.cleaned_data["calle"]
    
    def clean_localidad(self):
        if not self.cleaned_data["localidad"].isalpha():
            raise ValidationError("El nombre de la localidad solo puede estar compuesto por letras")

        return self.cleaned_data["localidad"]

    def clean(self):
        cleaned_data = super().clean()
        nombre=cleaned_data.get("nombre")
        apellido=cleaned_data.get("apellido")
        calle=cleaned_data.get("calle")
        localidad=cleaned_data.get("localidad")

        if nombre == "Carlos" and apellido == "Lopez":
            raise ValidationError("El usuario ya existe")
        
        if self.cleaned_data["dni"] < 1000000:
            raise ValidationError("El DNI debe tener 8 digitos")
        
        return self.cleaned_data"""
# Mascotas
especies = (
    ("1", "Perro"),
    ("2", "Gato"),
    ("3", "Otros")
)

tamaños = (
    ("1", "Chico"),
    ("2", "Mediano"),
    ("3", "Grande")
)

razas = (
    ("1", "Raza"),
    ("2", "Mestizo")
)

mantos = (
    ("1", "Claro"),
    ("2", "Oscuro")
)

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=20, required=True)
    #apellido = forms.CharField(label="Apellido", max_length=20, required=True)  
    edad = forms.IntegerField(label="Edad", required=True) 
    especie = forms.ChoiceField(label="Especie", required=True, choices=especies)
    tamaño = forms.ChoiceField(label="Tamaño", required=True, choices=tamaños)
    tipo = forms.ChoiceField(label="Tipo", required=True, choices=razas)
    manto = forms.ChoiceField(label="Manto", required=True, choices=mantos)
    castracion = forms.CharField(label="Castracion", max_length=200, required=True)
    
    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["nombre"]

class AdopcionFormulario(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = '__all__'

        error_messages = {
            'dni': {
                'required': 'El campo DNI es Obligatorio ☺'
            }
        }

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")
        return self.cleaned_data["nombre"]
