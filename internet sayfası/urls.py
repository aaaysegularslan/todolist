  
from django.urls import path
from . import views




urlpatterns = [
  
    
    path("", views.home, name= 'home'),
    path("item/", views.item, name= 'item'),
    path("about/",views.about, name='about'),
    path("information/",views.information, name='information'),
    path('createlist/',views.createlist, name="createlist"),
    path('home/<ToDoList_id>',views.deletelist, name="deletelist"),
    path('createitem/',views.createitem, name="createitem"),
    path('completed/<Item_id>',views.completed, name="completed"),
    path('not_completed/<Item_id>',views.not_completed, name="not_completed"),

    

  

    







]
