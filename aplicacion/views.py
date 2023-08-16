from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Post

# Class Based View
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Mixin - decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

#Turnos
@login_required
def turnos(request):
    ctx = {"turnos": Turno.objects.all() }
    return render(request, "aplicacion/turnos.html", ctx)


def turnoForm(request):
    # preguntar si viene metodo post 
    if request.method == "POST":   
        miForm = TurnoForm(request.POST)
        if miForm.is_valid():
            turno_nombre = miForm.cleaned_data.get('nombre')
            turno_dni = miForm.cleaned_data.get('dni')
            turno_especialidad = miForm.cleaned_data.get('especialidad')
            turno = Turno(nombre=turno_nombre, dni=turno_dni, especialidad=turno_especialidad)
            turno.save()
            return redirect('turnos')
    else:
        miForm = TurnoForm()

    return render(request, "aplicacion/turnoForm.html", {"form":miForm})

# Lógica para obtener y mostrar los turnos despues de form
def vista_turnos(request):    
    turnos = Turno.objects.all()
    return render(request, "aplicacion/turnos.html", {"turnos": turnos})

# Buscador
def buscar(request):
    return render(request, "aplicacion/buscar.html")

# Click va a buscar2
def buscar2(request):
    nombre = request.GET.get('nombre')
    if nombre:
        especialidades = Especialidad.objects.filter(nombre__icontains=nombre)
        if especialidades:
            return render(request, "aplicacion/resultadosBuscar.html", {"nombre": nombre, "especialidades": especialidades})
        else:
            mensaje = f"No se encontraron resultados para '{nombre}'."
            return render(request, "aplicacion/resultadosBuscar.html", {"mensaje": mensaje})
    else:
        mensaje = "Por favor, ingrese un nombre para buscar."
        return render(request, "aplicacion/resultadosBuscar.html", {"mensaje": mensaje})

# Blog
def lista_posts(request):
    posts = Post.objects.order_by('-fecha_publicacion')
    return render(request, "aplicacion/lista_posts.html", {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "aplicacion/detalle_post.html", {'post': post})


# Perfil User
@login_required
def perfil(request):
    return render(request, "aplicacion/perfil.html")

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')            
            usuario.save()
            return render(request, "aplicacion/perfil.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario) #llama los datos del user
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username}) 


# - Class Based View -

# Especialidad
def especialidades(request):
    ctx = {"especialidades": Especialidad.objects.all() }
    return render(request, "aplicacion/especialidad.html")

class EspecialidadList(ListView):
    model = Especialidad

class EspecialidadCreate(LoginRequiredMixin, CreateView):
    model = Especialidad
    fields = ['nombre', 'doctor']    
    success_url = reverse_lazy('especialidad') 
    # reverse_lazy (al name del url)

class EspecialidadDetail(DetailView):
    model = Especialidad

class EspecialidadUpdate(LoginRequiredMixin, UpdateView):
    model = Especialidad
    # campos que toma
    fields = ['nombre', 'doctor']
    # redirecciona 
    success_url = reverse_lazy('especialidad') 

class EspecialidadDelete(LoginRequiredMixin, DeleteView):
    model = Especialidad
    # redirecciona 
    success_url = reverse_lazy('especialidad')     

 

# Login, logout, Register

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
    # Guardar el Avatar try-except               
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                # retornar y enviar mensaje con el user
                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})    

# Registro de Usuario:
def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # ex UserCreationForm 
        if form.is_valid():  # ok validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() # ex UserCreationForm 

    return render(request, "aplicacion/registro.html", {"form": form})


# Avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #_Esto es para borrar el avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si esto es verdad quiere decir que hay un Avatar previo
                avatarViejo[0].delete()

            #_ Graba avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_Almacena en session la url del avatar en base
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})