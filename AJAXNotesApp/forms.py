from django import forms
from django.forms.widgets import Textarea

class addNote(forms.Form):
    title = forms.CharField(max_length = 50)

class addDescription(forms.Form):
    description = forms.CharField(widget = Textarea(attrs = {'rows': 10}))
