from django.shortcuts import render, redirect
from .models import List
from django.http import HttpResponseRedirect


def home(request):
    todo_items = List.objects.all()
    return render(request, 'todo.html', {'todo_items': todo_items})


def addtodo(requset):
    x = requset.POST['title']
    new_item = List(title=x)
    new_item.save()
    return HttpResponseRedirect('/')


def deletetodoview(request, i):
    y = List.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/')


