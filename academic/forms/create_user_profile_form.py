from django import forms
from academic.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'user_id': 'User ID',
            'bio': 'Biography',
            'website': 'Website URL',
        }
        help_texts = {
            'bio': 'Enter a brief biography.',
            'website': 'Enter your personal or professional website URL.',
        }
        error_messages = {
            'user_id': {
                'unique': "A user profile with this User ID already exists.",
            },
        }
