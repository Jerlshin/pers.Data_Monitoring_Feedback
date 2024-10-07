from django import forms
from .models import UserInput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['read_bible', 'prayed', 'exercised', 'satisfied', 'hurt_someone', 'loved_someone', 'daily_summary']
        widgets = {
            'daily_summary': forms.Textarea(attrs={'maxlength': 500}),
        }
