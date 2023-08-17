
# Proyecto Final - CODERHOUSE Comisión 43862
Desarrollo de una aplicación web utilizando el framework Django de Python para una clínica denominada 'Health-Center'. La aplicación ofrece diversas funcionalidades, entre las que se incluyen registro de pacientes, solicitud de turnos médicos, edición de información personal con opción de agregar una imagen de perfil/avatar, búsqueda de especialidades médicas y una implementación lógica de la interacción de botones para realizar el inicio de sesión o cierre de sesión, usando bloques condicionales en Django Template Language (DTL). 

![captura web](https://github.com/Alef2k/Alejandro-Fernandez43865/blob/master/captura_web.jpg)

## Secciones de la Web:
- Inicio 
- Turno
- Especialidad
- Blog
- Mi perfil (Acerca de mí)


. Se utiliza y se adapta un template de boostrap.<br>
. Formulario de busqueda al menú que busca los nombres de las especialidades.<br>
. Formulario para agregar un turno, para agregar especialidad (con CRUD), registrar usuarios (con CRUD).

## Video de uso:
https://www.youtube.com/watch?v=wdv2y99-3qU

## Detalle de los Modelos:

### Turno:
- Propósito: Simulación para solicitar turnos médicos y revisar el historial (requiere registro).
- Campos: Nombre, DNI, Especialidad.

### Especialidad:
- Propósito: Representa diversas especialidades médicas.
- Campos: 
  - Nombre: Nombre de la especialidad médica.
  - Doctor: Nombre del médico especialista en dicha área.

### Categoria:
- Propósito: Representa las categorías para las publicaciones de un blog.
- Campos: 
  - Nombre: Nombre de la categoría.
  - Descripcion: Descripción de la categoría.

### Post:
- Propósito: Modelo para las publicaciones de un blog.
- Campos: 
  - Título: Título de la publicación.
  - Contenido: Contenido del post.
  - Fecha de Publicación: Fecha y hora de la publicación.
  - Autor: Autor de la publicación.
  - Categoría: Relaciona con el modelo Categoria mediante su clave primaria.

### Avatar:
- Propósito: Representa los avatares e imágenes de perfil de usuarios registrados.
- Campos:
  - Imagen: Imagen del avatar.
  - Usuario: Usuario registrado asociado al avatar.

## Casos de test:
![Casos_de_test_AF.xlsx](https://github.com/Alef2k/Alejandro-Fernandez43865/blob/master/Casos_de_test_AF.jpg)


## Usuario web:
user: alef2k <br>
Login: 081076Alef2k

## Administración de Django
> `localhost:8000/admin` <br>
user: alef2 <br>
login: 081076Alef2k


## CONFIGURACIÓN:

1. Crea una carpeta en tu computadora y dento de ésta debes clonar el Repositorio

> `git clone https://github.com/Alef2k/Alejandro-Fernandez43865`

o descomprimir el zip **Alejandro-Fernandez43865-master.zip** 

2. En la direccion de la carpeta donde esta descomprimido el proyecto escribir `cmd` para abrir la consola y luego desde la consola `code .` para abrir el VScode.

3. Abierto el Visual Studio Code 
escribir en la terminal 
> `python manage.py runserver`
***En Mac cambiar python por python3***

4. Ingresa en el Browser de tu preferencia e ingresa a la siguiente dirección: 
> `http:\\localhost:8000`

Listo!!! ya tenemos funcionando nuestra App.


## BASE DE DATOS 
Base de datos `(bd_clinica.db)` 

## Entorno de trabajo:
#### Python 3.11.4
#### Django 4.2.4

#### Package  Version:
- asgiref  3.7.2 
- Django   4.2.4
- Pillow   10.0.0
- sqlparse 0.4.4
- tzdata   2023.3


