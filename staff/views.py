from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Staff_member
from .forms import StaffModelForm


class StaffListView(LoginRequiredMixin, generic.ListView):
    template_name = "staff/staff_list.html"
    
    def get_queryset(self):
        return Staff_member.objects.all()


class StaffCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "staff/staff_create.html"
    form_class = StaffModelForm

    def get_success_url(self):
        return reverse("staff:staff-list")

    def form_valid(self, form):
        staff = form.save(commit=False)
        print(self.request.user)
        # staff.organisation = self.request.user.userprofile
        # staff.save()
        return super(StaffCreateView, self).form_valid(form)
