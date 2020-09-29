import datetime
from django.db import models

class Habit(models.Model):
    goal = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"{self.goal}"














