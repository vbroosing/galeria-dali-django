Verificar que la version de python es:
Python 3.12.5

En el "simbolo del sistema"
ejecutar comando de entorno virtual:
cd venv/Scripts
activate
cd ../..

en una terminal de bash ejecutar:
source venv/Scripts/activate

una vez estes en la ruta:
C:\...\pruebaBack>

verificar la siguiente version de django instalada e el entorno virtual:
asgiref==3.8.1
Django==5.1.1
sqlparse==0.5.1
tzdata==2024.1

luego ejecutar:
py manage.py runserver

En el navegador de preferencia ir a 
localhost:8000/