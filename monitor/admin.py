# monitor/admin.py
from django.contrib import admin
from .models import UserInput, CalendarTask

admin.site.register(UserInput)

@admin.register(CalendarTask)
class CalendarTaskAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'task_type', 'priority']
    list_filter = ['task_type', 'priority']
    search_fields = ['name']
    