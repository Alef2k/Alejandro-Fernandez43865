from django.contrib import admin
from .models import Turno, Especialidad, Avatar, Categoria, Post

# Register your models here.
admin.site.register(Turno)
admin.site.register(Especialidad)
admin.site.register(Avatar)
admin.site.register(Categoria)
admin.site.register(Post)