from django.contrib import admin

from .models import Work

class WorkAdmin(admin.ModelAdmin):
    list_per_page = 10
    readonly_fields=['slug']
    search_fields = ['title', 'content']
    list_filter = ['created_at']

admin.site.register(Work, WorkAdmin)