from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'view_full_name', 'username', 'email', 'view_phone_number']

    # Add users
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
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

    view_full_name.short_description = 'ФИО'


admin.site.register(CustomUser, CustomUserAdmin)
