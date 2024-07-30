from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import ShortNotesForm
from .models import Short_notes

def notes_view(request):
    if request.method == 'POST':
        form = ShortNotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_view')
    else:
        form = ShortNotesForm()
    
    notes = Short_notes.objects.all().order_by('-created_at')
    return render(request, 'study_notes/notes.html', {'form': form, 'notes': notes})

