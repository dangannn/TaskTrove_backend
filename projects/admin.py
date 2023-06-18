from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project, ProjectRequest


class ProjectAdmin(ModelAdmin):
    model = Project
    list_display = ['id', 'name', 'description', 'pub_date', 'customer']
    date_hierarchy = 'pub_date'
    filter_horizontal = ['freelancer']
    list_filter = ['customer', 'freelancer']
    # добавление в редактировании поиска по m2m
    raw_id_fields = ["freelancer"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectRequest)
