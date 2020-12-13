
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import request
from .models import ToDoList,Item
from .forms import ListForm,Lists



def home (request):
    listname=ToDoList.objects.all()
    context={'listname':listname}
    return render(request, "webpage/home.html", context )

def item (request):
    name=Item.objects.all()
    context={'name':name}
    return render(request, "webpage/items.html", context )



    


def about (request):
    return render(request, "webpage/about.html")





def information (request):
    return render(request, "webpage/information.html")




def createlist(request):
    if request.method =="POST":
        form=Lists(request.POST or None)
        if form.is_valid:
            form.save()
            createlist=ToDoList.objects.all()
            return render(request,"webpage/createlist.html",{'createlist':createlist})

    else:   
     createlist=ToDoList.objects.all()
     return render(request,"webpage/createlist.html",{'createlist':createlist})





def deletelist(request,ToDoList_id):
    deletelist=ToDoList.objects.get(pk=ToDoList_id)
    deletelist.delete()
  
    return render(request, "webpage/home.html")







def createitem(request):

    if request.method =="POST":
        form=ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            createitem=Item.objects.all()
            return render(request, "webpage/items.html",{'createitem':createitem})
           
    else:   
     createitem=Item.objects.all()
     return render(request,"webpage/createitem.html",{'createitem':createitem})





def completed(request,Item_id):
    item=Item.objects.get(pk=Item_id)
    item.completed= True
    item.save()
    return redirect("home")

def not_completed(request,Item_id):
    item=Item.objects.get(pk=Item_id)
    item.completed = False
    item.save()
    return redirect("home")





