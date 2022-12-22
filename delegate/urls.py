
from django.contrib import admin
from django.urls import path, include


app_name = 'leads'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads'))

]
