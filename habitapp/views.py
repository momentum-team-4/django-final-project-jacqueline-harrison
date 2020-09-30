from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm
from .models import HabitRecord
import datetime as dt
from django.core.serializers import serialize
import json


@login_required
def all_habits(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/all_habits.html', {"habits": habits})

@login_required
def display_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    
    if HabitRecord.objects.filter(habit=habit, date=dt.date.today()):
        makeButton = False

    else:
        makeButton = True

    habit_records = HabitRecord.objects.filter(habit=pk)
    habit_records_serial = serialize("json", habit_records)
    print(habit_records_serial)

    return render(request, 'habits/display_habit.html', {"habit": habit, "makeButton": makeButton, "serial_habit": habit_records_serial})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "GET":
        form = HabitForm(instance=habit)

    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()

            success(request, 'habit updated')

        return redirect (to='all_habits')

    return render(request, "habits/edit_habit.html", {"form":form})


@login_required
def add_habit(request):
    if request.method == "GET":
        form = HabitForm
    
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()

        success(request, 'Habit created')
        return redirect(to='all_habits')
    
    return render(request, 'habits/add_habit.html', {"form": form})


@login_required
def log_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    new_record = HabitRecord(habit=habit)
    new_record.save()
    success(request, "Great work! Your task has been logged.")

    return redirect(to='display_habit', pk=pk)

@login_required
def delete_habit(request, pk):
    if request.method == "GET":
        return render(request, "habits/delete_habit.html")

    else:
        habit = get_object_or_404(Habit, pk=pk)
        habit.delete()
        success(request, 'habit deleted')

        return redirect(to='all_habits')

    return render(request, "habits/all_habits.html", {"form": form})



