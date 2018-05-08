import json
from django.shortcuts import render
from job.forms.job import JobForm
from job.models.job import JobField

def index(request):
    template = 'index.html'

    if request.method == 'GET':
        form = JobForm()
        return render(request, template, {'form': form})
    else:
        post_data = request.POST.copy()
        form = JobForm(post_data)
        job = None
        if form.is_valid():
            job = form.save()
        return render(request, template, {
            'form': form,
            'job': job
        })

def login(request):
    template = 'login.html'

    if request.method == 'GET':
        return render(request, template)

def register(request):
    template = 'register.html'

    if request.method == 'GET':
        return render(request, template)