from django import forms
from leads.models import Staff_member


class StaffModelForm(forms.ModelForm):
    class Meta:
        model = Staff_member
        fields = (
            'user',
            'organisation'
        )
