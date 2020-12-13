from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,request











def login_view(request):
    
       form = LoginForm(request.POST or None)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user= authenticate(request=request,username=username, password=password)
           login(request, user)
           return redirect('home')
    
       return render(request,'login/login.html',{"form": form}) 






