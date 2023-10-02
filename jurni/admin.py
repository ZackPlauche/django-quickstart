from django.contrib import admin

from . import models

@admin.register(models.Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title']

