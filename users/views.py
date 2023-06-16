from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.serializers import ProjectRequestSerializer
from ratings.serializers import CommentSerializer, FavoriteListSerializer
from users.models import CustomUser
from users.serializers import UserSerializer


class UsersView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'], name='comments_list', url_path='comments')
    def comments_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset[user_id].freelancer_comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='favorite_list', url_path='favorite_list')
    def favorite_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset[user_id].favorite_list.all()
        serializer = FavoriteListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='requests_list', url_path='requests')
    def requests_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset[user_id].freelancer_requests.all()
        serializer = ProjectRequestSerializer(queryset, many=True)
        return Response(serializer.data)
