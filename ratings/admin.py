from django.contrib import admin
from .models import Comment, FavoriteList

admin.site.register(Comment)
admin.site.register(FavoriteList)
