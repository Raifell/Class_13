from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'create_at', 'deadline', 'status', 'completed_at', 'slug')


admin.site.register(Task, TaskAdmin)
