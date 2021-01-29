from django.shortcuts import render, redirect
from .forms import addNote
from .models import Note

def viewNotes(request):
    noteForm = addNote
    context = {
        'noteForm': noteForm,
        'notes': Note.objects.all()
    }
    return render(request, 'html/home.html', context)

def noteAdd(request, noteID):
    if request.method == 'POST':
        add_note = Note.objects.get(id = noteID)
        add_note.description = request.POST['description']
        add_note.save()
    return render(request, 'html/notes.html')

def titleAdd(request):
    newTitle = addNote(request.POST)
    if request.method == 'POST':
        if newTitle.is_valid():
            Note.objects.create(
                title = newTitle.cleaned_data['title']
            )
    return render(request, 'html/notes.html')

def deleteNote(request, noteID):
    if request.method == 'POST':
        note2delete = Note.objects.get(id = noteID)
        note2delete.delete()
    return render(request, 'html/notes.html')