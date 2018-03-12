from django.contrib import admin
from admin.forms.job import JobFieldForm

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'question_contact', 'is_posted')

class JobFieldAdmin(admin.ModelAdmin):
    form = JobFieldForm
    list_display = ('name', 'slug')