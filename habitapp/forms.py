from django import forms
from .models import Habit
from .models import HabitRecord

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'goal'
        ]

class HabitRecordForm(forms.ModelForm):
    class Meta:
        model = HabitRecord
        fields = [
        ]