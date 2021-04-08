from django import forms
from . models import Project,Profile


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','image','description','link')
        
        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'description':forms.TextInput(attrs = {'class':'form-control'}),
            'link':forms.TextInput(attrs = {'class':'form-control'}),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email','bio','profile_pic')
        
        widgets = {
            'email': forms.TextInput(attrs = {'class': 'form-control'}),
            'bio': forms.Textarea(attrs = {'class': 'form-control'}),
        }