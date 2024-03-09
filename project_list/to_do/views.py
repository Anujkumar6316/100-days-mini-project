from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        todo_list = Task.objects.filter(user=request.user)
        return render(request, 'to_do/index.html', {'todo_list':todo_list})
    return render(request, 'to_do/index.html')

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'to_do/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'to_do/register.html', {'form':form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do:index')
        
    else:
        form = TaskForm()
    return render(request, 'to_do/add_task.html', {'form':form})

def details(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'to_do/details.html', {'to_do':task})

def edit(request,id):
    task=Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('to_do:index')
        
    else:
        form = TaskForm(instance=task)
    return render(request, 'to_do/edit.html', {'form':form})

def remove(request, id):
    to_be_remove=Task.objects.get(id=id)
    to_be_remove.delete()
    return redirect('to_do:index')