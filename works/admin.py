from django.contrib import admin
from .models import Work, WorkImage


class WorkImageInline(admin.StackedInline):
    model = WorkImage
    max_num=10
    extra=0


class WorkAdmin(admin.ModelAdmin):
    list_per_page = 10
    readonly_fields=['slug']
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    inlines = [WorkImageInline]

admin.site.register(Work, WorkAdmin)