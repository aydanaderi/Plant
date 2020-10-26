from __future__ import unicode_literals
from django.contrib import admin
from . import models

@admin.register(models.Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    list_filter = ('username','email')
    search_fields = ('username','email')