from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('added_time', 'updated_time', 'assigned_to')
