from django.shortcuts import render, redirect, HttpResponse
from models import NoteManager
from django.core import serializers
import json

def index(request):
    return render(request, 'notes/index.html')
def show_notes(request):
    notes = NoteManager.objects.all()
    return HttpResponse(serializers.serialize("json", notes), content_type='application/json')
def create(request):
    note = NoteManager.objects.create(note = request.POST.get('note', False), description = request.POST.get('description', False))
    return HttpResponse(json.dumps({'note': note.note, 'description': note.description, 'id': note.id}), content_type='application/json')
def edit(request):
     note = NoteManager.objects.get(id = request.POST.get('id'))
     note.description = request.POST.get('description', '')
     note.save()
     return HttpResponse(json.dumps({'note': note.note, 'description': note.description, 'id': note.id}), content_type='application/json')
def delete(request):
    id = request.POST.get('id')
    note = NoteManager.objects.get(id = id)
    note.delete()
    return HttpResponse(json.dumps({'note': note.note, 'description': note.description, 'id': id}), content_type='application/json')
