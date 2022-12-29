from django.urls import path
from .views import StaffListView, StaffCreateView, StaffDetailView, StaffUpdateView, StaffDeleteView


app_name = 'staff'

urlpatterns = [
    path('', StaffListView.as_view(), name='staff-list'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('<int:pk>/update/', StaffUpdateView.as_view(), name='staff-update'),
    path('<int:pk>/delete/', StaffDeleteView.as_view(), name='staff-delete'),
    path('create/', StaffCreateView.as_view(), name='staff-create'),

]
