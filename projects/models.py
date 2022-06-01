from django.db import models
import random

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    client = models.CharField(null=True, blank=True, max_length=50)
    key_feature_1 = models.CharField(max_length=20, blank=True)
    key_feature_2 = models.CharField(max_length=20, blank=True)
    key_feature_3 = models.CharField(max_length=20, blank=True)
    key_feature_4 = models.CharField(max_length=20, blank=True)
    key_feature_5 = models.CharField(max_length=20, blank=True)
    key_feature_6 = models.CharField(max_length=20, blank=True)
    tech_stack_1 = models.CharField(max_length=20, blank=True)
    tech_stack_2 = models.CharField(max_length=20, blank=True)
    tech_stack_3 = models.CharField(max_length=20, blank=True)
    tech_stack_4 = models.CharField(max_length=20, blank=True)
    tech_stack_5 = models.CharField(max_length=20, blank=True)
    tech_stack_6 = models.CharField(max_length=20, blank=True)
    github = models.CharField(max_length=100, blank=True)
    deployed = models.CharField(max_length=100, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    color_id = models.IntegerField(default=random.randint(1,6))

    def __str__(self) -> str:
        return self.name
