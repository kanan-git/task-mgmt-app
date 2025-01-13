from django.contrib import admin

from tasks.models import Task, Category, TypeOfTask

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(TypeOfTask)
