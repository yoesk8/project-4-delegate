from django import forms


class TaskForm(forms.Form):
    task_name = forms.CharField()
    task_description = forms.CharField()
    task_priority = forms.IntegerField(min_value=1)
