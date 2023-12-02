from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import *
from .forms import *


def task_list(request):
    tasks = Task.objects.filter(status='In progress')
    context = {
        'title': 'Main',
        'tasks': tasks,
    }
    return render(request, 'main/index_main.html', context)


def task_history(request):
    tasks = Task.objects.filter(status='Completed')
    context = {
        'title': 'History',
        'tasks': tasks,
    }
    return render(request, 'main/index_history.html', context)


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


def task_update(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    form = AddTaskForm(initial={'title': task.title,
                                'description': task.description,
                                'priority': task.priority,
                                'deadline': task.deadline,
                                'status': task.status,
                                'image': task.image})
    if request.method == 'POST':
        form = AddTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {
        'title': 'Update',
        'form': form,
    }
    return render(request, 'main/index_update.html', context)


def task_info(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    context = {
        'title': 'Info',
        'task': task,
    }
    return render(request, 'main/index_info.html', context)


def task_delete(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    task.delete()
    return redirect('task_list')


def task_complete(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    task.status = 'Completed'
    task.completed_at = datetime.now()
    task.save()
    return redirect('task_list')


def task_return(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)
    task.status = 'In progress'
    task.completed_at = None
    task.save()
    return redirect('task_list')

