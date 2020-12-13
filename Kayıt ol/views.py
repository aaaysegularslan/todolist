from django.contrib.admin.decorators import register
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate
from django.http import request






def registerPage(request):
    register=CreateUserForm()
    

    if request.method=='POST':
        register=CreateUserForm(request.POST)
        if register.is_valid():
            register.save()


    context={'register':register}
    return render (request,'register/register.html',context)




