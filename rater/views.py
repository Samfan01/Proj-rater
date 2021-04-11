from django.shortcuts import render,redirect,get_object_or_404
from .models import Project,Profile,Review
from .forms import NewProjectForm,ProfileForm,RateForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

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


def rate(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    user = request.user.profile
    reviews = Review.objects.filter(project=project_id)
    
    design_rate_average = reviews.aggregate(Avg("design_rate"))["design_rate__avg"]
    if design_rate_average == None:
        design_average = 0
    else:
        design_average = round(design_rate_average,1)

    usability_rate_average = reviews.aggregate(Avg("usability_rate"))["usability_rate__avg"]
    if usability_rate_average == None:
        usability_average = 0
    else:
        usability_average = round(usability_rate_average,1)

    content_rate_average = reviews.aggregate(Avg("content_rate"))["content_rate__avg"]
    if content_rate_average == None:
        content_average = 0
    else:    
        content_average = round(content_rate_average,1)

    sum = design_average+usability_average+content_average
    average = round(int(sum)/3,2)
    
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.project = project
            rate.save()
            return redirect('home')
    else:
        form = RateForm()
        
    template_name = 'rate.html'
    
    return render(request,template_name,{'form':form,'project':project,'reviews':reviews,'design_average':design_average,'usability_average':usability_average,'content_average':content_average,'average':average})