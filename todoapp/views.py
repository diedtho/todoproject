from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect

def todoappView(request):
    return render(request, 'todolist.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

def shiftUpTodoView(request, x):
    y = TodoListItem.objects.get(id= x[0])
    z = TodoListItem.objects.get(id= x[1])
    new_item = TodoListItem(content = z)
    new_item = TodoListItem(content = y)
    y.delete
    z.delete

    return HttpResponseRedirect('/todoapp/')