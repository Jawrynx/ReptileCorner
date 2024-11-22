from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'image']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        }