from django.db import models
from developers.models import Developer
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    developers = models.ManyToManyField(Developer, related_name='projects')
