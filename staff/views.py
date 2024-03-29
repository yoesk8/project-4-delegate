import random
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Staff_member
from .forms import StaffModelForm
from .mixins import OrganisorAndLoginRequiredMixin


class StaffListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "staff/staff_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)


class StaffCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "staff/staff_create.html"
    form_class = StaffModelForm

    def get_success_url(self):
        return reverse("staff:staff-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_manager = True
        user.is_staff = False
        user.set_password(f"{random.randint(0, 100000)}")
        user.save()
        Staff_member.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject="Invitation to join a team on Delegate",
            message="You have been invited to join a team on Delegate!",
            from_email="admin@t.com",
            recipient_list=[user.email]
        )
        # staff.organisation = self.request.user.userprofile
        # staff.save()
        return super(StaffCreateView, self).form_valid(form)


class StaffDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "staff/staff_detail.html"
    context_object_name = "staff"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)


class StaffUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "staff/staff_update.html"
    form_class = StaffModelForm
    context_object_name = "staff"

    def get_success_url(self):
        return reverse("staff:staff-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)


class StaffDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "staff/staff_delete.html"
    context_object_name = "staff"

    def get_success_url(self):
        return reverse("staff:staff-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Staff_member.objects.filter(organisation=organisation)
