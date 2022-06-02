from django.shortcuts import get_object_or_404, render
from .models import Blog

def blogs(request):
    blogs = Blog.objects.all().order_by('-created').filter(is_published=True)
    context = {
        'blogs': blogs,
    }
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blogs/blog.html',context)