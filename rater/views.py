from django.shortcuts import render,redirect
from .models import Project
from .forms import NewProjectForm

# Create your views here.

def home(request):
    projects = Project.get_projects()
    template_name = 'home.html'
    title = 'Project-Rator : Where You Rate and get Your Project Rated on.'
    return render(request,template_name,{'title':title,'projects':projects})

def new_project(request):
    model = Project
    form = NewProjectForm
    template_name = 'new_project.html',
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        
        return render(request,template_name,{'form':form})
    