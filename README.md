
Pasos para construir un contenedor Docker:

1. Crea un archivo de Dockerfile con las instrucciones de construcción.

2. Abre una terminal y navega hasta el directorio que contiene el Dockerfile.

3. Ejecuta el siguiente comando para construir la imagen de Docker:
    docker-compose build
    
Ejecuta el siguiente comando para iniciar los contenedores según la configuración especificada en el archivo:
  docker-compose up


Ejecuta el siguiente comando para listar los contenedores en ejecución y obtener el ID o el nombre del contenedor al que deseas acceder:
  docker ps
  
Copia el ID o el nombre del contenedor.

Ejecuta el siguiente comando para ingresar a la shell del contenedor:
  docker exec -it nombre_del_contenedor /bin/bash
  
Reemplaza "nombre_del_contenedor" por el ID o el nombre del contenedor que copiaste en el paso anterior.

Una vez dentro del contenedor, puedes ejecutar los comandos de Django para realizar las migraciones, como:
  python manage.py migrate users , despues ejecutar las migraciones normales : python manage.py makemigrations seguido despues python manage.py migrate
  
 Asegúrate de que el entorno de tu proyecto Django esté configurado correctamente y estés en el directorio raíz del proyecto.

Abre una terminal y ejecuta el siguiente comando para ingresar a la shell de Django:
    python manage.py shell

Dentro de la shell de Django, ejecuta los siguientes comandos para crear el usuario administrador:
  from django.contrib.auth import get_user_model
  User = get_user_model()
  User.objects.create_superuser('admin', 'carlos@gmail.com', 'Inicio*2023')
  
  
Starting development server at http://0.0.0.0:9000/

Api Root
http://localhost:9000/api/


iR ALA URL : http://0.0.0.0:9000/api/auth/login/

![image](https://github.com/carlosvisbal/Blog-Django-REST-framework-definitivo/assets/56123169/7edfb049-684f-4f72-9709-371891c4b177)


{
  "email": "carlos@gmail.com",
  "password": "Inicio*2023"
}

iNGRESAR LAS CREDENCIALES PARA TENER ACCESO A TODOS LOS MODULOS.





  
  
 



