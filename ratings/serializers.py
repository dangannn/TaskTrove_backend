from rest_framework.serializers import ModelSerializer

from ratings.models import Comment, FavoriteList


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'description', 'freelancer', 'pub_date']


class FavoriteListSerializer(ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ['customer', 'freelancer']
