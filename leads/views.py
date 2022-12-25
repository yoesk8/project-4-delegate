from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Staff_member
from .forms import TaskForm, TaskModelForm


def landing_page(request):
    return render(request, "landing.html")


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


def task_create(request):
    form = TaskModelForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/task_create.html", context)


def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskModelForm(instance=task)
    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "task": task
    }
    return render(request, "leads/task_update.html", context)


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("/leads")

# def task_update(request, pk):
#     task = Task.objects.get(id=pk)
#     form = TaskForm()
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task_name = form.cleaned_data["task_name"]
#             task_description = form.cleaned_data["task_description"]
#             task_priority = form.cleaned_data["task_priority"]
#             department = form.cleaned_data["department"]
#             staff_asigned = Staff_member.objects.first()
#             task.task_name = task_name
#             task.task_description = task_description
#             task.task_priority = task_priority
#             task.department = department
#             task.staff_asigned = staff_asigned
#             task.save()
#             return redirect("/leads")

    # context = {
    #     "form": form,
    #     "task": task
    # }
    # return render(request, "leads/task_update.html", context)

# Without django modelform
# def task_create(request):
    # form = TaskForm()
    # if request.method == "POST":
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         task_name = form.cleaned_data["task_name"]
    #         task_description = form.cleaned_data["task_description"]
    #         task_priority = form.cleaned_data["task_priority"]
    #         department = form.cleaned_data["department"]
    #         staff_asigned = Staff_member.objects.first()
    #         Task.objects.create(
    #             task_name=task_name,
    #             task_description=task_description,
    #             task_priority=task_priority,
    #             department=department,
    #             staff_asigned=staff_asigned
    #         )
    #         return redirect("/leads")

#     context = {
#         "form": form
#     }
#     return render(request, "leads/task_create.html", context)