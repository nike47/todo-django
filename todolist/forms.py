from django import forms
from django.forms import ModelForm

from .models import *

class TodoListForm(forms.ModelForm):

    class Meta:
        model=Todolist
        fields='__all__'

    text = forms.CharField(max_length=50,
    widget = forms.TextInput(attrs={'placeholder':'Enter todo e.g. Wash my car','type':'text'})
    )





    
