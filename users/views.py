from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success, error
from .forms import UserCreationForm
from .models import User


def create_user(request):
    if request.method == "GET":
        form = UserCreationForm()

    else:
        form= UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()

            success(request, 'Login created')
            return redirect(to='login_user')

    return render(request, 'accounts/create_user.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            success(request, 'Logged in Successfully')
            return redirect(to='all_habits')

        else:
            error(request, 'username or password does not exist')

    return render(request, 'accounts/login_user.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect(to='login_user')

