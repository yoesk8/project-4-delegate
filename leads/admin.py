from django.contrib import admin

from .models import User, Task, Staff_member, UserProfile, Category


admin.site.register(User)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Staff_member)
