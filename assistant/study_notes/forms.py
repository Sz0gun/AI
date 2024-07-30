from django import forms
from .models import Short_notes

class ShortNotesForm(forms.ModelForm):
    class Meta:
        model = Short_notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tytuł'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Treść notatki'}),
        }
