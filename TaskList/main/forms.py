from django import forms
from main.models import *


class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'deadline', 'status', 'image')
        widgets = {
            'deadline': forms.TextInput(attrs={'type': 'datetime-local'})
        }
