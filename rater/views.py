from django.shortcuts import render

# Create your views here.

def home(request):
    template_name = 'home.html'
    title = 'Project-Rator : Where You Rate and get Your Project Rated on.'
    return render(request,template_name,{'title':title})