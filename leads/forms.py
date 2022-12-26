from django import forms
from .models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'task_name', 
            'task_description',
            'task_priority',
            'department',
            'staff_asigned'
        )


class TaskForm(forms.Form):
    task_name = forms.CharField()
    task_description = forms.CharField()
    task_priority = forms.IntegerField(min_value=1)
    department = forms.CharField()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
