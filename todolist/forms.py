from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import ToDo

class TaskForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ["task"]

        widgets = {
            "task": forms.CheckboxSelectMultiple(),
        }
