from django.db import models
from datetime import datetime





class ToDoList(models.Model):
    	name=models.CharField(max_length=200)


    	def __str__(self):
    		return self.name




class Item(models.Model):
	todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	itemname=models.CharField(max_length=100)
	description =models.TextField(max_length=1000, blank=True)
	date=models.DateTimeField(default=datetime.now,blank=True)
	completed=models.BooleanField(default=False)


	def __str__(self):	
			return self.itemname







