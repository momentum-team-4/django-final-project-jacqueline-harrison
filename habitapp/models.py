from django.db import models

class Habits(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    goal = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    integer = models.IntegerField(null=False, blank=False)


