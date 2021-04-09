from django import forms
from . models import Project,Profile,Review,RATE_CHOICES


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
        
class RateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review','design_rate','usability_rate','content_rate')
        
        
        widgets = {
            'review': forms.Textarea(attrs={'class':'form-control'}),
            'design_rate':forms.Select(choices=RATE_CHOICES),
            'usability_rate':forms.Select(choices=RATE_CHOICES),
            'content_rate':forms.Select(choices=RATE_CHOICES)
        }