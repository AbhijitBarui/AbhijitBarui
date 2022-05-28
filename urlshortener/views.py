from django.shortcuts import redirect, render
from .models import UrlData
import uuid

def index(request):
    return render(request, 'urlshortener/urlshort.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        slug = str(uuid.uuid4())[:5]
        url = UrlData(slug=slug,link=link)
        url.save()
        data = slug
    context = {
        'data':data,
    }
    return render(request, 'urlshortener/urlshort.html', context)

def real(request, slug):
    real_url = UrlData.objects.get(slug=slug)
    if real_url:
        return redirect(real_url.link)
    else:
        return redirect('/')