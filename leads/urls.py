from django.urls import path
from .views import task_list, task_detail

app_name = 'leads'


urlpatterns = [
    path('', task_list),
    path('<pk>/', task_detail),
]
