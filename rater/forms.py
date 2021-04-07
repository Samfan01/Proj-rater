from django import forms
from . models import Project


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','image','description','link')
        
        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'description':forms.TextInput(attrs = {'class':'form-control'}),
            'link':forms.TextInput(attrs = {'class':'form-control'}),
        }