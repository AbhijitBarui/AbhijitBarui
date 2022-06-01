from django.shortcuts import render
from projects.models import Project

colors = ['blue','green','red','orange','purple','pink']

def index(request):
    projects = Project.objects.all().order_by('-created')[:3]
    context = {
        'projects': projects,
        'color': colors,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')