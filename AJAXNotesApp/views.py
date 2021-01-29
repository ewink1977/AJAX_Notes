from django.shortcuts import render
from .forms import addNote, addDescription
from .models import Note

def viewNotes(request):
    noteForm = addNote(auto_id = False)
    descForm = addDescription(auto_id = False)
    context = {
        'noteForm': noteForm,
        'descForm': descForm,
        'notes': Note.objects.all()
    }
    return render(request, 'html/home.html', context)

def noteAdd(request, noteID):
    pass

def titleAdd(request):
    pass

def deleteNote(request, noteID):
    pass