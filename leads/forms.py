from django import forms
from .models import Task, Staff_member, UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name',
                  'task_description',
                  'task_priority',
                  'organisation',
                  'staff_asigned',
                  'category']


class TaskForm(forms.Form):
    task_name = forms.CharField()
    task_description = forms.CharField()
    task_priority = forms.IntegerField(min_value=1)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class AssignStaffForm(forms.Form):
    staff_asigned = forms.ModelChoiceField(queryset=Staff_member.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        print(request.user)
        staffs = Staff_member.objects.filter(organisation=request.user.userprofile)
        super(AssignStaffForm, self).__init__(*args, **kwargs)
        self.fields["staff_asigned"].queryset = staffs

