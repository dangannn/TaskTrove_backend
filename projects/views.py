from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import ProjectSerializer
from users.serializers import UserSerializer


class ProjectsView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'], name='freelancers', url_path='freelancers')
    def freelancers_list(self, request, pk):
        project_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset[project_id].freelancer.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
