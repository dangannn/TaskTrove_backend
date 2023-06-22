from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Comment, FavoriteList


class CommentAdmin(ModelAdmin):
    model = Comment
    list_display = ['id', 'author', 'is_positive', 'pub_date', 'description']
    date_hierarchy = 'pub_date'
    filter_horizontal = ['freelancer']
    list_filter = ['author', 'freelancer']
    # добавление в редактировании поиска по m2m
    raw_id_fields = ["freelancer"]


admin.site.register(Comment, CommentAdmin)
admin.site.register(FavoriteList)
