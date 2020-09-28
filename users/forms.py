from django.contrib.auth.forms import UserCreationForm as _UserCreationForm
from django import forms
from .models import User

class UserCreationForm(_UserCreationForm):
    class Meta(_UserCreationForm.Meta):
        model = User
        fields = _UserCreationForm.Meta.fields