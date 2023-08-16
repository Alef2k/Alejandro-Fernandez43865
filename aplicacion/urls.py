from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

# cursos
urlpatterns = [
    path('', index, name="inicio"),
    path('turnos/', turnos, name="turnos"), 
    path('turnoForm/', turnoForm, name="turnoForm"),

    path('buscar/', buscar, name="buscar"),
    path('buscar2/', buscar2, name="buscar2"),

# Especialidad
    path('especialidad/', EspecialidadList.as_view(), name="especialidad"),
    path('create_especialidad/', EspecialidadCreate.as_view(), name="create_especialidad"),
    path('detail_especialidad/<int:pk>/', EspecialidadDetail.as_view(), name="detail_especialidad"),
    path('update_especialidad/<int:pk>/', EspecialidadUpdate.as_view(), name="update_especialidad"),
    path('delete_especialidad/<int:pk>/', EspecialidadDelete.as_view(), name="delete_especialidad"),

# Blog

    path('lista_posts/', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),






# Login
    path('login/', login_request, name="login"),  
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),  
    path('register/', register, name="register"),

# Perfil
    path('perfil/', perfil, name="perfil"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),   

# Agregar Avatar
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]
