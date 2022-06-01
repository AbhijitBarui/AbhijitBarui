from django.shortcuts import get_object_or_404, render
from .models import Project

colors = ['blue','green','red','orange','purple','pink']

def projects(request):
    projects = Project.objects.all().order_by('-created')
    context = {
        'projects': projects,
        'color': colors,
    }
    return render(request, 'projects/projects.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project,
    }
    return render(request, 'projects/project.html', context)