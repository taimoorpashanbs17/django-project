# django-project

Its Sample Django Project running on Docker with user management handled.

Clone git Project:

`git clone https://github.com/taimoorpashanbs17/django-project.git`

Move to folder: 

`cd django-project`

Start Running the project with Simple Docker :

`docker build .`

Run Docker Compose with Having all docker components:

`docker-compose build `


Do Migrations:

`docker-compose run app sh -c "python manage.py makemigrations core"`

Run All Test:

`docker-compose run app sh -c "python manage.py test"`