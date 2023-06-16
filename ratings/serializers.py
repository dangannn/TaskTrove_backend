from rest_framework.serializers import ModelSerializer

from ratings.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'description', 'freelancer']
