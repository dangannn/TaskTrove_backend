from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Project, ProjectRequest


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project

    def dehydrate_name(self, project):
        return project.name.upper()

    def get_export_queryset(self):
        return self.get_queryset().filter(pub_date__year=2023)

    def filter_export(self, queryset, **kwargs):
        queryset = queryset.order_by('id')
        return queryset


class ProjectAdmin(ImportExportModelAdmin, ModelAdmin):
    model = Project
    resource_class = ProjectResource
    list_display = ['id', 'name', 'pub_date', 'urgency', 'payment', 'customer_link', 'view_freelancer']
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

    def customer_link(self, obj):
        customer = obj.customer
        if customer:
            url = reverse('admin:users_customuser_change', args=[customer.id])
            return format_html('<a href="{}">{}</a>', url, customer)
        return None

    customer_link.short_description = 'Customer'


class ProjectRequestAdmin(ModelAdmin):
    model = ProjectRequest
    list_display = ['id', 'name', 'pub_date', 'customer_link', 'view_freelancer']
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

    def customer_link(self, obj):
        customer = obj.customer
        if customer:
            url = reverse('admin:users_customuser_change', args=[customer.id])
            return format_html('<a href="{}">{}</a>', url, customer)
        return None

    customer_link.short_description = 'Customer'


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectRequest, ProjectRequestAdmin)
