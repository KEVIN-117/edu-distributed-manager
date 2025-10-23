from django import forms
from academic.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'bio': 'Biography',
            'website': 'Website URL',
        }
        help_texts = {
            'bio': 'Enter a brief biography.',
            'website': 'Enter your personal or professional website URL.',
        }
