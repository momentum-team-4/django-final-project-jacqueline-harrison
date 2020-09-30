import datetime
from django.db import models
from users.models import User

class Habit(models.Model):
    # goal_name = models.CharField(max_length=255, null=False, blank=False)
    goal = models.CharField(max_length=255, null=False, blank=False)
    # goal_number = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    # below intention is to have many-to-one relation b/t user table and habit table using foreign key. we know
    #this is not right as is but not sure how to relate them to one another. 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #above is uncommented for bug fix attempt 

   
class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = [['habit', 'date']]

    #need to be able to add record for previous days
    #add html for display_habit page to show via colors
    #add a11y functionality


    def __str__(self):
        return f"{self.goal}"

