from django.contrib import admin
from django.contrib.admin import ModelAdmin

from info.models import News


class NewsAdmin(ModelAdmin):
    model = News
    list_display = ['id', 'author', 'pub_date', 'name']
    list_display_links = ['id', 'name']
    date_hierarchy = 'pub_date'
    search_fields = ["name"]
    list_filter = ['author']


admin.site.register(News, NewsAdmin)
