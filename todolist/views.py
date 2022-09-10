from urllib import request
from django.shortcuts import render, redirect
from .models import ToDo

def todolistPage(request):
    todo = ToDo.objects.all()

    unfinished = ToDo.objects.filter(finished="False")
    finished = ToDo.objects.filter(finished="True")
    
    context= {
        "todo": todo,
        "finished": finished,
        "unfinished": unfinished,
    }

    return render(request, "todolist/todolist.html", context)

def createTask(request):
    text = request.POST["task"]
    task = ToDo(task=text)
    task.save()

    return redirect("todo-list")

def deleteTask(request, pk):
    task = ToDo.objects.get(id=pk) 
    task.delete()
        
    return redirect("todo-list")

def check(request, pk):
    task = ToDo.objects.get(id=pk)
    task.finished = True
    task.save()
    return redirect("todo-list")

def uncheck(request,pk):
    task = ToDo.objects.get(id=pk)
    task.finished = False
    task.save()

    return redirect("todo-list")
