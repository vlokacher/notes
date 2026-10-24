from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/create.html", {"form": form})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/detail.html", {"note": note})
