from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render (request, 'tasks/task_list.html', {'task': tasks})

def add_task(request):
    if request.method == 'POST':
        titulo = request.POST.get('litle')
        if titulo:
            Task.objects.create(title=titulo)
        return redirect('task_list')
    return render(request, 'task/add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

# Create your views here.
