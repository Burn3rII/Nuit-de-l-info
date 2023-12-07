from django.contrib import admin
from .models import Task, Email, User, DiffusionList

admin.site.register(Task)
admin.site.register(Email)
admin.site.register(User)
admin.site.register(DiffusionList)
