from django import forms
from .models import Habits

class HabitForm(forms.HabitForm):
    class Meta:
        model = Habits
        fields = [
            'goal',
            'date'
        ]