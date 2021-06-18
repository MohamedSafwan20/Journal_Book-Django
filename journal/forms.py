from django import forms
from .models import Journal


class AddJournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = [
            'title',
            'journal_content',
            'key_moments',
        ]
        labels = {
            'title': ('Title'),
            'journal_content': ('Body'),
            'key_moments': ('Special Moments'),
        }
        widgets = {
            'key_moments': forms.Textarea(attrs={'placeholder': "Seperate each moment with ','"})
        }
