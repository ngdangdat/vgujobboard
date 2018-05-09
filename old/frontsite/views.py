import json
from django.shortcuts import render
from job.forms.job import JobForm
from job.models.job import JobField
from user.forms import RegisterForm, ProfileForm, PasswordResetForm
from django.urls import reverse_lazy, reverse

from django.contrib import messages
from django.contrib.auth.views import \
    (
        PasswordResetView as BasePasswordResetView,
        PasswordResetDoneView as BasePasswordResetDoneView,
        PasswordResetConfirmView as BasePasswordResetConfirmView,
        PasswordResetCompleteView as BasePasswordResetCompleteView,
    )
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

def index(request):
    template = 'index.html'
    context = {}
    if request.user and request.user.is_authenticated:
        if request.method == 'GET':
            form = JobForm()
            context['form'] = form
        else:
            post_data = request.POST.copy()
            form = JobForm(post_data)
            job = None
            if form.is_valid():
                job = form.save()
            context['job'] = job
        context['form'] = form
    else:
        template = 'login.html'
    return render(request, template, context)

def register(request):
    template = 'register.html'
    context = {}

    if request.method == 'GET':
        user_form = RegisterForm()
        profile_form = ProfileForm()
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return render(request, template, context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.save(user=user)
            return HttpResponseRedirect('/')
        return render(request, template, context)


def login(request):
    template = 'login.html'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                user_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, template, {'message': "Your account is disabled."})
        else:
            return render(request, template, {'message': "Invalid login details supplied."})
    else:
        return render(request, template, {})

def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')

class PasswordResetView(BasePasswordResetView):
    template_name = 'forgot_password.html'
    email_template_name = 'email/password_reset_email.html'
    success_url = reverse_lazy('frontsite:password_reset_done')

class PasswordResetDoneView(BasePasswordResetDoneView):
    template_name = 'password_reset_done.html'

class PasswordResetConfirmView(BasePasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('frontsite:password_reset_complete')

class PasswordResetCompleteView(BasePasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
