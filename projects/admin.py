from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project, ProjectRequest


class ProjectAdmin(ModelAdmin):
    model = Project
    list_display = ['id', 'name', 'pub_date', 'customer', 'view_freelancer']
    list_display_links = ['id', 'name']
    date_hierarchy = 'pub_date'
    # filter_horizontal = ['freelancer']
    list_filter = ['customer', 'freelancer']
    # добавление в редактировании поиска по m2m
    raw_id_fields = ["freelancer"]
    # readonly_fields = ["name", "description"]
    search_fields = ["name"]

    @admin.display(empty_value="-")
    def view_freelancer(self, obj):
        if len([*obj.freelancer.values()]) > 0:
            return [*obj.freelancer.values()][0]['first_name'] + " " + [*obj.freelancer.values()][0]['last_name']

    view_freelancer.short_description = 'фрилансер'


class ProjectRequestAdmin(ModelAdmin):
    model = ProjectRequest
    list_display = ['id', 'name', 'pub_date', 'customer', 'view_freelancer']
    list_display_links = ['id', 'name']
    date_hierarchy = 'pub_date'
    # filter_horizontal = ['freelancer']
    list_filter = ['customer', 'freelancer']
    # добавление в редактировании поиска по m2m
    raw_id_fields = ["freelancer"]
    # readonly_fields = ["name", "description"]
    search_fields = ["name"]

    @admin.display(empty_value="-")
    def view_freelancer(self, obj):
        if len([*obj.freelancer.values()]) > 0:
            return [*obj.freelancer.values()][0]['first_name'] + " " + [*obj.freelancer.values()][0]['last_name']

    view_freelancer.short_description = 'фрилансер'


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectRequest, ProjectRequestAdmin)
