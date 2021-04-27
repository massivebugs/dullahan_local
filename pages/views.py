from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def home_view(req, *args, **kwargs):
    return render(req, 'home.html')


def about_view(req, *args, **kwargs):
    return render(req, 'about.html')

# Authentication specific views

def log_in(req):
    form = AuthenticationForm()
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            login(req, form.get_user())
            return redirect(reverse('get_home'))
        else:
            return render(req, 'login.html', {'form': form})
    return render(req, 'login.html', {'form': form})

@login_required
def log_out(req):
    logout(req)
    return redirect(reverse('log_in'))


def sign_up(req):
    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(data=req.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('log_in'))
        else:
            print(form.errors)
    return render(req, 'signup.html', {'form': form})
