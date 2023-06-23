from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.serializers import ProjectRequestSerializer, ProjectSerializer
from ratings.models import FavoriteList
from ratings.serializers import CommentSerializer, FavoriteListSerializer
from users.models import CustomUser
from users.serializers import UserSerializer, FreelancerSerializer, CustomerSerializer


class UsersView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'], name='comments_list', url_path='comments')
    def comments_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset().filter(id=user_id)
        queryset = queryset[0].freelancer_comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='requests_list', url_path='requests')
    def requests_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset[user_id].freelancer_requests.all()
        serializer = ProjectRequestSerializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['get'], name='projects', url_path='projects')
    # def projects_list(self, request, pk):
    #     user_id: int = int(pk)  # Получение значения аргумента id из pk
    #     queryset = self.get_queryset()
    #     queryset = queryset[user_id].freelancer_projects.all()
    #     serializer = ProjectSerializer(queryset, many=True)
    #     return Response(serializer.data)


class FreelancersView(ModelViewSet):
    queryset = CustomUser.objects.filter(groups=1)
    serializer_class = FreelancerSerializer


class CustomersView(ModelViewSet):
    queryset = CustomUser.objects.filter(groups=2)
    serializer_class = CustomerSerializer
