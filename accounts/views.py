from django.shortcuts import render

# Create your views here.
# accounts/views.py
from .forms import EmailForm, SignUpForm
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
 
from accounts.models import Email
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if email_form.is_valid() and not signup_form.is_valid():
            email_to_confirm = email_form.cleaned_data.get('email')
            if not Email.objects.all().filter(email=email_to_confirm):
                messages.error(request, 'Email not in Directory')
            elif User.objects.all().filter(email=email_to_confirm):
                messages.error(request, 'Email already registered')
            else:
                return render(request, 'signup.html', {'form': signup_form})
        elif email_form.is_valid() and signup_form.is_valid():
            signup_form.save()
            return HttpResponseRedirect('/')
        return render(request, 'signup.html', {'form': email_form})
    else:
        email_form = EmailForm()
        return render(request, 'signup.html', {'form': email_form})
