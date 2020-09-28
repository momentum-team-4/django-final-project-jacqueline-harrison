from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success, error
from .models import Habits

def all_habits(request):
    pass

def display_habit(request, pk):
    pass



def edit_habit(request, pk):
    pass



def delete_habit(request, pk):
    pass


def add_habit(request):
    pass
