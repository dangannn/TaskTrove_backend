from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000)


class Response(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000)
    project = models.ManyToManyField(Project)
