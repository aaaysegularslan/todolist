

from django.urls import path
from django.contrib.auth import login, views 
from . import views







urlpatterns = [
  
    path('', views.login_view, name='login'),
    



]
