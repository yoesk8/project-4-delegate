from django.urls import path
from .views import task_list, task_detail, task_create

app_name = 'leads'


urlpatterns = [
    path('', task_list),
    path('create/', task_create),
    path('<pk>/', task_detail),
]
