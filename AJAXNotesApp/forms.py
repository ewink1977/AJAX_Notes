from django import forms
from django.forms.widgets import TextInput, Textarea

class addNote(forms.Form):
    title = forms.CharField(
        max_length = 50,
        label = '',
        widget = TextInput(attrs={
            'placeholder': 'Insert note title here...'
            })
    )