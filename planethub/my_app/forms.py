from django import forms
from .models import Mission

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['type', 'date']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a start date',
                    'type': 'date'
                }
            ),
        }