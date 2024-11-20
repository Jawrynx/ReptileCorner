from django import forms
from .models import Reptile

class ReptileForm(forms.ModelForm):
    class Meta:
        model = Reptile
        fields = ['name', 'age', 'bio', 'reptile_picture']