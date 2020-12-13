
from django import forms
from .models import Item, ToDoList


class Lists(forms.ModelForm):
    
    class Meta:
        model=ToDoList
        fields=["name"]





class ListForm(forms.ModelForm):
    
    class Meta:
        model=Item
        fields=["itemname","description","date","completed"]
      

