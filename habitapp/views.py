from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from .models import Habit
from .forms import HabitForm


def all_habits(request):
    habits = Habit.objects.all()
    return render(request, 'habits/all_habits.html', {"habits": habits})

def display_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'habits/display_habit.html', {"habit": habit})


def add_habit(request):
    if request.method == "GET":
        form = HabitForm
    
    else:
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save

        success(request, 'Habit created')
        return redirect(to='all_habits')
    
    return render(request, 'habits/add_habit.html', {"form": form})


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

    return render(request, "habits/edit_habit.html"), {"form":form}



def delete_habit(request, pk):
    if request.method == "GET":
        return render(request, "habits/delete_habit.html")

    else:
        habit = get_object_or_404(Habit, pk=pk)
        habit.delete()
        success(request, 'habit deleted')

        return redirect(to='all_habits')

    return render(request, "habits/all_habits.html", {"form": form})



