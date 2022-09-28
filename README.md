# Punto de venta en Django.


## Requisitos el sistema.

* PostgreSQL
* Python3
* pip


## Primeros pasos para descargar el proyecto.

Para descargar el proyecto lo que se requiere es tener instalado git en tu máquina; esto para que 
la descarga del mismo sea más sencilla.   
Cuando se deseé descargar el repositorio, se deberá abrir la terminal y escribir el comando 
`git clone https://github.com/HectrollXD/PuntoDeVenta.git`.   
Y posterior a esto, procedemos a navegar hasta la carpeta con el comando `cd PuntoDeVenta` y 
procedemos a crear el entorno virtual para ejecutarlo.


## Crear entorno virtual.

Para crear el entorno virutal debemos de navegar hasta la carpeta del proyecto mediante consola.   
Una vez dentro de la carpeta, realizaremos el comando 
`python3 -m venv <nombre de entorno virtual a crear>`.   
Cuando este sea creado, procedemos a activar el entorno virtual con el comando 
`source <nombre del entorno virtual>/bin/activate` y procedemos a instalar las dependencias 
necesarias para correr el sistema. Para ello es necesario ejecutar el comando 
`pip install -r requirements.txt`. Todo esto tomando en cuenta que debe de estar activo el entorno 
virutal que ccreamos para el proyecto.


## Arrancar el proyecto.

Antes de arrancar el proyecto, es necesario crear la base de datos y el usuario para poder 
crear las tablas. Para ello se debem ejecutar los scripts SQL que están en el archivo db.sql.  
Una vez que estos son creados, se deberá cambiar los datos de conexión de la base de datos desde el 
archivo `./sell_point/settings.py`.   
Cuando éste se encuentre con la configuración correcta, se deberá de ejecutar el comando 
`python3 manage.py makemigrations` y `python3 manage.py migrate`. En caso que este no genere las 
tablas de la base de datos, es necesario borrar las migraciones desde las carpetas de cada 
aplicación. Solo se debe de dejar el archivo llamado `__init__.py` y `0001_initial.py` y se procede 
a ejecutar nuevamente los comandos anteriores.   
Una vez realizadas las migraciones, se deberar de ejecutar el comando `python3 manage.py runserver` 
para arrancar el servidor.


# Funcionalidades recomendadas para crear en el proyecto:
* Separar la vista "crear cuentas" del homepage.
* En el homepage: Mostrar la estadística de los productos (notificar si un producto llegó o está 
por debajo de la columna "int_deseable_stock" de la tabla "catalog_products").
* Crear vista para aumetar el stock de los productos e ir guardando los registros en una tabla para 
que sea posible registrar las compras.