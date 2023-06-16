from rest_framework.viewsets import ModelViewSet

from ratings.models import Comment
from ratings.serializers import CommentSerializer


class CommentsView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticated,)


