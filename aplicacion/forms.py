from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TurnoForm(forms.Form):
    ESPECIALIDAD = (
        ("Cardiología", "Cardiología"),
        ("Médico Clinico", "Médico Clinico"),
        ("Traumatología", "Traumatología"),
        ("Laboratorio", "Laboratorio"), 
        ("Pediatría", "Pediatría"), 
        ("Gastroenterología", "Gastroenterología"), 
        ("Nefrología", "Nefrología"), 

       
    )
    especialidad = forms.ChoiceField(label="Especialidad", choices=ESPECIALIDAD, required=True)
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    dni = forms.IntegerField(label="Dni", required=True, widget=forms.TextInput(attrs={'type': 'number'}))
       

# registro
class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # limpiar los help text
        help_texts = {k:"" for k in fields}   

# Edit User
class UserEditForm(UserCreationForm):    
    first_name = forms.CharField(label="Nombre", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User  # import User libreria
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2' ] 
        # quitar los help text
        help_texts = { k:"" for k in fields}        

# Avatar
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True) 