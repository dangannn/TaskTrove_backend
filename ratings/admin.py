from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Comment, FavoriteList


class CommentAdmin(ModelAdmin):
    model = Comment
    list_display = ['id', 'author', 'is_positive', 'pub_date', 'description', 'view_freelancer']
    list_display_links = ['id', 'description']
    date_hierarchy = 'pub_date'
    filter_horizontal = ['freelancer']
    list_filter = ['author', 'freelancer']
    # добавление в редактировании поиска по m2m
    raw_id_fields = ["freelancer"]
    # readonly_fields = ["email"]
    search_fields = ["author", "description", "freelancer"]

    @admin.display(empty_value="-")
    def view_freelancer(self, obj):
        if len([*obj.freelancer.values()]) > 0:
            return [*obj.freelancer.values()][0]['first_name'] + " " + [*obj.freelancer.values()][0]['last_name']

    view_freelancer.short_description = 'фрилансер'


class FavoriteListAdmin(ModelAdmin):
    model = FavoriteList
    list_display = ['id', 'customer']
    list_display_links = ['id', 'customer']
    # date_hierarchy = 'pub_date'
    filter_horizontal = ['freelancer']
    list_filter = ['customer']
    # добавление в редактировании поиска по m2m
    # raw_id_fields = ["freelancer"]
    # readonly_fields = ["email"]
    search_fields = ['customer']


admin.site.register(Comment, CommentAdmin)
admin.site.register(FavoriteList, FavoriteListAdmin)
