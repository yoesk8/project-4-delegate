from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Task, Staff_member
from .forms import TaskForm, TaskModelForm


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")


class TaskListView(generic.ListView):
    template_name = "leads/tasks_list.html"
    queryset = Task.objects.all()
    context_object_name = "tasks"


def task_list(request):
    task = Task.objects.all()
    context = {
        "tasks": task
    }
    return render(request, "leads/tasks_list.html", context)


class TaskDetailView(generic.DetailView):
    template_name = "leads/tasks_detail.html"
    queryset = Task.objects.all()
    context_object_name = "task"


def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        "task": task
    }
    return render(request, "leads/tasks_detail.html", context)


class TaskCreateView(generic.CreateView):
    template_name = "leads/task_create.html"
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("leads:task-list")


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


class TaskUpdateView(generic.UpdateView):
    template_name = "leads/task_update.html"
    queryset = Task.objects.all()

    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("leads:task-list")


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


class TaskDeleteView(generic.DeleteView):
    template_name = "leads/task_delete.html"
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse("leads:task-list")


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