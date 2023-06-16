from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ratings.serializers import CommentSerializer
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
