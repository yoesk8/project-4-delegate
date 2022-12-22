from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def task_list(request):
    task = Task.objects.all()
    context = {
        "tasks": task
    }
    return render(request, "leads/tasks_list.html", context)


def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        "task": task
    }
    return render(request, "leads/tasks_detail.html", context)
