from django.urls import path
from .views import StaffListView, StaffCreateView


app_name = 'staff'

urlpatterns = [
    path('', StaffListView.as_view(), name='staff-list'),
    path('create/', StaffCreateView.as_view(), name='staff-create'),

]
