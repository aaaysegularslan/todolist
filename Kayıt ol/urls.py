

from django.urls import path
from django.contrib.auth import login, views 
from . import views







urlpatterns = [
  
   
    path('', views.registerPage, name='register'),
]
