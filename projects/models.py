from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


class Project(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='project_customer')
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000)
    freelancer = models.ManyToManyField(CustomUser, related_name='freelancer_projects')

    def __str__(self):
        return self.name
