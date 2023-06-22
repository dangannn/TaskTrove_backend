from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ratings.models import Comment, FavoriteList
from ratings.serializers import CommentSerializer, FavoriteListSerializer
from users.serializers import FreelancerSerializer


class CommentsView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticated,)

    # @action(detail=True, methods=['get'], name='freelancers_list', url_path='comments')
    # def freelancers_list(self, request, pk):
    #     project_id: int = int(pk)  # Получение значения аргумента id из pk
    #     queryset = self.get_queryset()
    #     queryset = queryset[project_id].freelancer.all()
    #     serializer = CommentSerializer(queryset, many=True)
    #     return Response(serializer.data)


class FavoriteListsView(ModelViewSet):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
    # permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'], name='favorite_list', url_path='favorite_list')
    def favorite_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset().filter(customer=user_id)[0].freelancer
        # serializer = FavoriteListSerializer(queryset, many=True)
        serializer = FreelancerSerializer(queryset, many=True)
        return Response(serializer.data)
