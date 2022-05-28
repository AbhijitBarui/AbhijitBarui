from django.db import models

class UrlData(models.Model):
    link = models.CharField(max_length=500)
    slug = models.CharField(max_length=10)