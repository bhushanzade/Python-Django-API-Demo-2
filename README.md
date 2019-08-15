# Python-Django-Rest-API-Demo-2
How we write web services / rest api using python django rest framework

# Steps for Django Rest Api

1) Download Python 3.4.3

2) set environment variables in advance setting

   - C:\Python3.4;
   - C:\Python3.4\Scripts;

3) download get-pip.py   to install pip in windowns

4) run this get-pip.py using cmd and go to path where the file is downloaded

    install step    -python get-pip.py

5) need virtual environment

    - pip install virtualenvwrapper-win

6) now create virtual environment

    - mkvirtualenv project_name

    e.g   mkvirtualenv demo

7) open demo in cmd

8) If new need to activate the demo project

    - workon demo

9) install django within virtual env project
   - pip install django
   - pip install django-rest-framework

10) create django project on cmd path set demo project path

   - django-admin startproject project_name

	e.g. django-admin startproject myproject

11) open myprojectin cmd and run manage.py server

    - python manage.py runserver


# Your Django Started...............

# For demo how api written in django we create Song table api

12) under myproject create app using command

    -   django-admin startapp api

13) add serialiezers.py file under api folder

	from django.contrib.auth.models import User
	from rest_framework import serializers
	from .models import Songs

	class SongsSerializer(serializers.HyperlinkedModelSerializer):
	    class Meta:
        	model = Songs
	        fields = ('id','title','desc','year')

14) change views.py 
	
	from django.contrib.auth.models import User, Group
	from rest_framework import viewsets
	from .serializers import SongsSerializer
	from .models import Songs

	class SongsViewSet(viewsets.ModelViewSet):
	    queryset = Songs.objects.all()
	    serializer_class = SongsSerializer

15) install pip install django-cors-headers for handling cors origin errors

16) add line in setting.py file

	CORS_ORIGIN_WHITELIST = ['http://localhost:4200'] // this is your frontend framework server name.

    also add initialized app name within the Installed_Apps

		'demo.api',
       	        'corsheaders',
		'rest_framework',

   also add this line in middleware
	'corsheaders.middleware.CorsMiddleware',

17) change in urls.py file 

	from django.contrib import admin
	from django.urls import include, path
	from rest_framework import routers
	from demo.api import views

	router = routers.DefaultRouter()
	router.register(r'songs', views.SongsViewSet)

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include(router.urls)),
	    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	]

18) changes on model.py file

	from django.db import models

	class Songs(models.Model):
	    title = models.CharField(max_length=32)
	    desc = models.CharField(max_length=256)
	    year = models.IntegerField()

19) register model in admin.py file

	from .models import Songs

	Register your models here.

	sadmin.site.register(Songs)

20) python manage.py makemigrations     this will need when new migration of database

21) python manage.py migrate 1st this process after setup django api project and also use after migration

# Finally we create Songs table under this python NoSQL database we can check CRUD operations using postman or directly added in frontend framework. Here we check on postman

1) Donwload Postman if not available in your PC Link here https://www.getpostman.com/downloads/

2) We check all CRUD operations here

3) Create/Post request method

Add Songs under the songs table set POST method and add this url http://127.0.0.1:8000/songs/   and set headers like
	Key= Content-Type     &    value= application/json
under the Body use raw data and add this content
{
  "title":"On my Way",
  "desc":"Alan Walker Song",
  "year":"2019"
}
and send the form to check result.

4) Get request method
set GET method and add this url http://127.0.0.1:8000/songs/ and send to check the results

5) GET by ID request method 
set GET method and add this url http://127.0.0.1:8000/songs/1 and send to check the results

6) PUT request method for update perticular object
set PUT method and add this url http://127.0.0.1:8000/songs/1/   and set headers like
	Key= Content-Type     &    value= application/json
under the Body use raw data and add this content
{
  "title":"Tiger zinda hai",
  "desc":"Salman khan movie song",
  "year":"2012"
}
and send the form to check result.

7) DELETE request by ID
set DELETE method and add this url http://127.0.0.1:8000/songs/1/ and send to check the results

# Thank You...


