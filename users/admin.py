from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from projects.models import Project
from .models import CustomUser


class ProjectsInline(admin.TabularInline):
    model = Project


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'view_full_name', 'username', 'email', 'view_group']
    list_display_links = ['id', 'view_full_name', 'email']
    date_hierarchy = 'date_joined'
    filter_horizontal = ['groups']
    list_filter = ['groups']
    readonly_fields = ["email"]
    search_fields = ["username"]

    inlines = [ProjectsInline]

    # Add users
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'phone_number',
                    'description',
                    'groups',
                )
            }
        )
    )

    # Edit user
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'phone_number',
                    'description',
                )
            }
        )
    )

    @admin.display(empty_value="-")
    def view_phone_number(self, obj):
        return obj.phone_number

    view_phone_number.short_description = 'Телефон'

    @admin.display(empty_value="-")
    def view_full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    @admin.display(empty_value="-")
    def view_group(self, obj):
        if len([*obj.groups.values()]) > 0:
            return [*obj.groups.values()][0]['name']

    view_group.short_description = 'группа'


admin.site.register(CustomUser, CustomUserAdmin)
