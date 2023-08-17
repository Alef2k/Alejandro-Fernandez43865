
# Proyecto Final - CODERHOUSE Comisión 43862
. Python - Framework Django
Aplicación web de una clinica "Health-Center" que contiene 5 modelos:<br>
1 Turno: (Simulación para sacar turno y revisar historial "Requiere estar registado") - Campos: Nombre, DNI, Especialidad.<br>

2 Especialidad: representa las diferentes especialidades médicas. Tiene los siguientes campos: Nombre: (nombre de la especialidad médica)
, doctor (almacena el nombre del médico especialista en esta área).<br>


3 Categoria: Representa las categorías para los posts de un blog. Campos: nombre, descripcion.<br>
4 Post: Este modelo representa una publicación en un blog que tiene los siguientes campos: titulo, contenido, fecha_publicacion, autor, categoria (relaciona el pk del modelo Categoria)<br>

5 Avatar: Este modelo representa los avatares de perfil de usuario. Tiene los siguientes campos: imagen, user. <br>

# Secciones de la Web:
- Inicio 
- Turno
- Especialidad
- Blog
- Mi perfil (Acerca de mí)


. Se utilizó un template de boostrap.<br>
. Se crea y de adapta un form de busqueda a la pagina pagina principal (base.html) que busca los nombres de las especialidades<br>
. Formularios para agregar un turno, para agregar especialidad (con CRUD), registrar usuarios (con CRUD).



# Usuario web:
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




