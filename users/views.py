from django.shortcuts import render
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

            success(request, 'login created')
            return redirect(to='login_user')

    return render(request, 'users/create_user.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            success(request, 'Logged in Successfully')
            login(request, user)
            redirect(to='display_habits')

        else:
            error(request, 'username/password does not exist')

    return render(request, 'users/login_user.html')


def logout_user(request):
    logout(request)
    redirect(to='login_user')

