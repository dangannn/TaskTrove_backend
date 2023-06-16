from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.models import Project, ProjectRequest
from projects.serializers import ProjectSerializer, ProjectRequestSerializer
from users.serializers import FreelancerSerializer


class ProjectsView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'], name='freelancers_list', url_path='freelancers')
    def freelancers_list(self, request, pk):
        project_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset[project_id].freelancer.all()
        serializer = FreelancerSerializer(queryset, many=True)
        return Response(serializer.data)


class ProjectRequestsView(ModelViewSet):
    queryset = ProjectRequest.objects.all()
    serializer_class = ProjectRequestSerializer

    # permission_classes = (IsAuthenticated,)

    # @action(detail=True, methods=['get'], name='requests_list', url_path='requests')
    # def requests_list(self, request, pk):
    #     project_id: int = int(pk)  # Получение значения аргумента id из pk
    #     queryset = self.get_queryset()
    #     queryset = queryset[project_id].freelancer.all()
    #     serializer = FreelancerSerializer(queryset, many=True)
    #     return Response(serializer.data)
