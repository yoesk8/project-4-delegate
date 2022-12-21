from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def home_page(request):
    task = Task.objects.all()
    context = {
        "tasks": task
    }
    return render(request, "leads/home.html", context)
