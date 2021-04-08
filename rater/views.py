from django.shortcuts import render,redirect
from .models import Project,Profile
from .forms import NewProjectForm,ProfileForm

# Create your views here.

def home(request):
    projects = Project.get_projects()
    template_name = 'home.html'
    title = 'Project-Rator : Where You Rate and get Your Project Rated on.'
    return render(request,template_name,{'title':title,'projects':projects})

def new_project(request):
    model = Project
    
    template_name = 'new_project.html',
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user.profile
            form.save()
            return redirect('home')
    else:
        form = NewProjectForm()
        
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
def profile(request):
    template_name = 'profile.html'
    projects = request.user.profile.project.all()
    
    
    return render(request,template_name,{'projects':projects})

def update_profile(request):
    model = Profile
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            post = form.save(commit=False)      
            post.save()
        return redirect('profile')
    else:
        form = ProfileForm
   
    template_name = 'update_profile.html',
    
    return render(request,template_name,{'form':form})


