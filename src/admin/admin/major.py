from django.contrib import admin
# from django import forms

class MajorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'shorten', 'start_from', )
    ordering = ('start_from', )
