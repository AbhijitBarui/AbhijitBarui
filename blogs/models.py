from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to = 'blogphotos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to = 'blogphotos/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return self.title[:20]
