from django import forms
from .models import Task


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
