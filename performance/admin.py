"""
Performance admin module
"""
from django.contrib import admin

from .models import Performance


class PerformanceAdmin(admin.ModelAdmin):
    """
    Performance admin
    """
    fields = ('name', 'photo', 'actors', 'producer', 'duration',
              'sort_description', 'description')
    list_display = ('name', 'sort_description')
    search_fields = ['name']


admin.site.register(Performance, PerformanceAdmin)
