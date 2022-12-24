from django.urls import path
from .views import task_list, task_detail, task_create, task_update

app_name = 'leads'


urlpatterns = [
    path('', task_list),
    path('create/', task_create),
    path('<int:pk>/', task_detail),
    path('<int:pk>/update/', task_update),
]
