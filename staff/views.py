from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Staff_member
from .forms import StaffModelForm


class StaffListView(LoginRequiredMixin, generic.ListView):
    template_name = "staff/staff_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)


class StaffCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "staff/staff_create.html"
    form_class = StaffModelForm

    def get_success_url(self):
        return reverse("staff:staff-list")

    def form_valid(self, form):
        staff = form.save(commit=False)
        staff.organisation = self.request.user.userprofile
        staff.save()
        return super(StaffCreateView, self).form_valid(form)


class StaffDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "staff/staff_detail.html"
    context_object_name = "staff"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)


class StaffUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "staff/staff_update.html"
    form_class = StaffModelForm
    context_object_name = "staff"

    def get_success_url(self):
        return reverse("staff:staff-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)


class StaffDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "staff/staff_delete.html"
    context_object_name = "staff"

    def get_success_url(self):
        return reverse("staff:staff-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)
