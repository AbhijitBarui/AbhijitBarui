from django.shortcuts import render
from projects.models import Project
from testimonials.models import Testimonial

colors = ['blue','green','red','orange','purple','pink']

def index(request):
    projects = Project.objects.all().order_by('-created')[:3]
    testimonials = Testimonial.objects.all().order_by('-created')
    context = {
        'projects': projects,
        'testimonials': testimonials,
        'color': colors,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')