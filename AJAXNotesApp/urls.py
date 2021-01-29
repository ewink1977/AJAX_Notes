from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewNotes, name = 'home'),
    path('add/note/<int:noteID>', views.noteAdd, name = 'addNote'),
    path('add/title', views.titleAdd, name = 'addTitle'),
    path('delete/note/<int:noteID>', views.deleteNote, name = 'deleteNote'),
]