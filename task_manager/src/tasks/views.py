from django.shortcuts import render
from django.http import HttpResponse
from . import models

def all_tasks(request):
    context = {
        'tasks': models.Task.objects.all()
    }
    return render(request, 'tasks/tasks.html', context)


def task(request, pk):
    context = {
    'task': models.Task.objects.filter(pk=pk).first()
    }
    return render(request, 'tasks/task.html', context)
