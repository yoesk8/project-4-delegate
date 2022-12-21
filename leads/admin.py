from django.contrib import admin

from .models import User, Task, Staff_member


admin.site.register(User)
admin.site.register(Task)
admin.site.register(Staff_member)
