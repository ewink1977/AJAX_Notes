from django import forms
from django.db import models
from django.db.models import fields
from django.forms.widgets import Textarea
from .models import Note

class addNote(forms.ModelForm):
    class Meta:
        models = Note
        fields = ('title')

class addDescription(forms.ModelForm):
    class Meta:
        models = Note
        fields = ('description')
        widgets = {
            'description': Textarea(attrs = {'cols': 50, 'rows': 20})
        }



