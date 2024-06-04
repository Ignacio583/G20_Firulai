from django import forms
from django.core.exceptions import ValidationError

viveEn = (
    ("1", "Casa"),
    ("2", "Casa Quinta"),
    ("3", "Departamento"),
    ("4", "Otro")
)

class FormularioAdop(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=20, required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'})) 
    apellido = forms.CharField(label="Apellido", max_length=20, required=True) 
    dni = forms.IntegerField(label="DNI", required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)
    calle = forms.CharField(label="calle", max_length=20, required=True)
    numero = forms.IntegerField(label="Número", required=True)
    localidad = forms.CharField(label="Localidad", max_length=20, required=True)
    viveEn = forms.ChoiceField(label="Vive en", required=True, choices=viveEn)
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
        
        return self.cleaned_data