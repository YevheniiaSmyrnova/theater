"""
Actor admin module
"""
from django.contrib import admin

from actor.models import Actor


class ActorAdmin(admin.ModelAdmin):
    """
    Actor admin
    """
    fields = ('first_name', 'last_name', 'photo', 'position')
    list_display = ('last_name', 'first_name', 'position')
    list_filter = ['first_name']
    search_fields = ['first_name', 'last_name']


admin.site.register(Actor, ActorAdmin)
