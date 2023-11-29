from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def task_list(request):
    tasks = Task.objects.filter(status='In progress')
    context = {
        'title': 'Main',
        'tasks': tasks,
    }
    return render(request, 'main/index_main.html', context)


def add_task(request):
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {
        'title': 'Create',
        'form': form,
    }
    return render(request, 'main/index_add.html', context)


def task_info(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    context = {
        'title': 'Info',
        'task': task,
    }
    return render(request, 'main/index_info.html', context)
