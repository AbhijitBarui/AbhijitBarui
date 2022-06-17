from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('routine/', include('routines.urls')),
    path('urlshort/', include('urlshortener.urls')),
    path('projects/', include('projects.urls')),
    path('blogs/', include('blogs.urls')),
    # path('testimonials/', include('testimonials.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
