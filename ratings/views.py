from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ratings.models import Comment, FavoriteList
from ratings.serializers import CommentSerializer, FavoriteListSerializer


class CommentsView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class FavoriteListsView(ModelViewSet):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = (IsAuthenticated,)
