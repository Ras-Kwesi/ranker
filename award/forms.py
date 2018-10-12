from django import forms
from .models import *



class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['likes', 'profile']