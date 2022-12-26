from django.urls import path
from .views import (
    task_list, task_detail, task_create, task_update, task_delete,
    TaskListView, TaskDetailView, TaskCreateView,
    TaskUpdateView, TaskDeleteView
)
app_name = 'leads'


urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
