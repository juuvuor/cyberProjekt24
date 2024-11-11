from django import forms
from .models import Entry


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']