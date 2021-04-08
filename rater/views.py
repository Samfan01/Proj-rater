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
    
def search_project(request):
    
    if 'title' in request.GET and request.GET['title']:
        search_term = request.GET.get('title')
        searched_projects = Project.search_by_title(search_term)
        message = f'{search_term}'
        
        return render(request, 'search.html',{'message':message,'projects':searched_projects})
    
    else:
        message = "You haven't searched for any item."
        return render(request,'search.html',{'message':message})
    