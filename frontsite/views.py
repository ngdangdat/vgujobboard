import json
from django.shortcuts import render
from job.forms.job import JobForm
from job.models.job import JobField

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

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

# def login(request):
#     template = 'login.html'

#     if request.method == 'GET':
#         return render(request, template)

def register(request):
    template = 'register.html'

    if request.method == 'GET':
        return render(request, template)

def user_login(request):
    template = 'login.html'

    if request.method == 'POST':
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check username/pw. Returns a User object or None
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        if user:
            if user.is_active:
                login(request, user)
                return render(request, template, {'message': "You are logged in successfully!"})
            else:
                return render(request, template, {'message': "Your account is disabled."})
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            # # Uncomment to create a dummy user and print all users on webpage
            # user = User.objects.create_user(username='user',
            #                      email='user@vgu.com',
            #                      password='your_password')
            # users = User.objects.all()
            # string = '-'.join([str(i) for i in users])
            # return render(request, template, {'message': string})
            return render(request, template, {'message': "Invalid login details supplied."})
    else:
        return render(request, template, {})
