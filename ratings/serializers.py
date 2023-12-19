from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ratings.models import Comment, FavoriteList


class CommentSerializer(ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['author', 'description', 'freelancer', 'pub_date', 'is_positive']

    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"


class FavoriteListSerializer(ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ['customer', 'freelancer']
