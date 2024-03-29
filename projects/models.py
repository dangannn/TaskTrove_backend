from django.contrib.auth.models import User
from django.db import models
from rest_framework import filters
from simple_history.models import HistoricalRecords

from users.models import CustomUser


class Project(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='projects')
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)
    urgency = models.DateField(max_length=1000, null=True)
    payment = models.IntegerField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    freelancer = models.ManyToManyField(CustomUser, related_name='freelancer_projects', blank=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name


class ProjectRequest(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name='request_customer')
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    freelancer = models.ManyToManyField(CustomUser, related_name='freelancer_requests')
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Запрос на проект"
        verbose_name_plural = "Запросы на проект"

    def __str__(self):
        return self.name
