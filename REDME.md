# Setup

- Asegurate que no exista la carpeta Modules/redirect/migrations  
- Prepara migrations: `python3 manage.py makemigrations redirect`  
- Ejecuta migrations: `python3 manage.py migrate`  
- Crea un super usuario: `python3 manage.py createsuperuser`  


- Inicia el servidor: `python3 manage.py runserver`  

- Asegurarse tener instalado memcached

- Url para pedir datos de los Redirects http://localhost:8000/get_redirect/<key>
- En caso de no tener ningun redirect crearlo desde la vista web admin de django

