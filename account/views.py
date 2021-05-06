from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from appointment.models import Payment
from django.contrib import messages
from userprofile.models import UserProfile


def logout_view(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('/')


def login_view(request):
    print(request.path, request.resolver_match.url_name)
    if request.method == 'POST':
        fm = LoginForm(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect('/')
            else:
                messages.warning(request, "Username and Password Incorrect")
        else:
            messages.warning(request, "Form is invalid")
    else:
        fm = LoginForm()
    return render(request, 'account/login.html', {'form': fm})


def signup(request):
    print('request', request.method)
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = user.first_name
            last_name = user.last_name
            name = first_name + ' ' + last_name
            UserProfile.objects.create(name=name, user=user)
            Payment.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registerd Successfully")
            return redirect('/')
        else:
            messages.warning(request, "Form is invalid")

    else:
        form = UserCreateForm()
    return render(request, 'account/signup.html', {'form': form})
