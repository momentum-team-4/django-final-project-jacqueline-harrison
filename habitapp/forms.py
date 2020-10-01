from django import forms
from .models import Habit
<<<<<<< HEAD
from.models import HabitRecord
=======
from .models import HabitRecord
>>>>>>> 9fd78820ea7124e3174e40d8c7511101db596df3

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'goal'
        ]

<<<<<<< HEAD

=======
>>>>>>> 9fd78820ea7124e3174e40d8c7511101db596df3
class HabitRecordForm(forms.ModelForm):
    class Meta:
        model = HabitRecord
        fields = [
<<<<<<< HEAD
        
=======
>>>>>>> 9fd78820ea7124e3174e40d8c7511101db596df3
        ]