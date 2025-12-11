from django.db import models
from developers.models import Developer
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projectss")
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    developers = models.ManyToManyField(Developer, related_name='projects')

    class Meta:
        permissions = [("detail_project", "Can see detail of projects")]
