from django import forms
from .models import *



class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['likes', 'profile']


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
        fields = ['profilepic','bio','contact']

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name', 'email']


class NewVote(forms.ModelForm):
    class Meta:
        model = Vote
        exclude = ['voter','project']