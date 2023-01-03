from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from staff.mixins import OrganisorAndLoginRequiredMixin
from .models import Task, Staff_member, Category
from .forms import TaskForm, TaskModelForm, CustomUserCreationForm, AssignStaffForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")


class TaskListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/tasks_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of tasks for the entire organisation
        if user.is_manager:
            queryset = Task.objects.filter(organisation=user.userprofile,
                                           staff_asigned__isnull=False)
        else:
            queryset = Task.objects.filter(organisation=user.staff_member.organisation,
                                           staff_asigned__isnull=False)
            # filter for the staff that is logged in, not working
            queryset = queryset.filter(staff_asigned__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_manager:
            queryset = Task.objects.filter(
                organisation=user.userprofile,
                staff_asigned__isnull=True
            )
            context.update({
                "unassigned_tasks": queryset
            })
        return context


def task_list(request):
    task = Task.objects.all()
    context = {
        "tasks": task
    }
    return render(request, "leads/tasks_list.html", context)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/tasks_detail.html"
    queryset = Task.objects.all()
    context_object_name = "task"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of tasks for the entire organisation
        if user.is_manager:
            queryset = Task.objects.filter(organisation=user.userprofile)
        else:
            queryset = Task.objects.filter(organisation=user.staff_member.organisation)
            print(queryset)
            # filter for the staff that is logged in, not working
            queryset = queryset.filter(staff_asigned__user=user)
        return queryset


def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        "task": task
    }
    return render(request, "leads/tasks_detail.html", context)


class TaskCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/task_create.html"
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("leads:task-list")

    def form_valid(self, form):
        send_mail(
            subject="A task has been created",
            message="Go to the site to see new task",
            from_email="test@test.com",
            recipient_list=["test@test2.com"]
            )
        return super(TaskCreateView, self).form_valid(form)


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


class TaskUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/task_update.html"
    form_class = TaskModelForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of tasks for the entire organisation
        return Task.objects.filter(organisation=user.userprofile)

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


class TaskDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/task_delete.html"

    def get_success_url(self):
        return reverse("leads:task-list")

    def get_queryset(self):
        user = self.request.user
        # initial queryset of tasks for the entire organisation
        return Task.objects.filter(organisation=user.userprofile)


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("/leads")


class AssignStaffView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_staff.html"
    form_class = AssignStaffForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignStaffView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:task-list")

    def form_valid(self, form):
        staff_asigned = form.cleaned_data["staff_asigned"]
        task = Task.objects.get(id=self.kwargs["pk"])
        task.staff_asigned = staff_asigned
        task.save()
        return super(AssignStaffView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_manager:
            queryset = Task.objects.filter(organisation=user.userprofile)
        else:
            queryset = Task.objects.filter(organisation=user.staff_member.organisation)

        context.update({
            "unassigned_tasks_count": queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        # initial queryset of tasks for the entire organisation
        if user.is_manager:
            # queryset = Category.objects.filter(organisation=user.userprofile)
            queryset = Category.objects.all()
        else:
            queryset = Category.objects.filter(organisation=user.staff_member.organisation)
        return queryset


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/category_detail.html"
    context_object_name = "category"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of tasks for the entire organisation
        if user.is_manager:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.staff_member.organisation)
        return queryset


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