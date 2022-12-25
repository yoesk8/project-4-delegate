from django.urls import path
from .views import task_list, task_detail, task_create, task_update, task_delete

app_name = 'leads'


urlpatterns = [
    path('', task_list, name='task-list'),
    path('create/', task_create, name='task-create'),
    path('<int:pk>/', task_detail, name='task-detail'),
    path('<int:pk>/update/', task_update, name='task-update'),
    path('<int:pk>/delete/', task_delete, name='task-delete'),
]
