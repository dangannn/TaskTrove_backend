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

    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'], name='projects', url_path='projects')
    def projects_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset.filter(customer=user_id)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='freelancers_list', url_path='freelancers')
    def freelancers_list(self, request, pk):
        project_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset().filter(id=project_id)[0]
        queryset = queryset.freelancer.all()
        serializer = FreelancerSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], name='add_freelancer', url_path='add_freelancer')
    def add_freelancer(self, request, pk, *args, **kwargs):
        project_id = int(pk)
        instance = self.get_queryset().filter(id=project_id)[0]
        partial = kwargs.pop('partial', False)
        request.data['freelancer'] += [_['id'] for _ in [*instance.freelancer.values()]]

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ProjectRequestsView(ModelViewSet):
    queryset = ProjectRequest.objects.all()
    serializer_class = ProjectRequestSerializer

    permission_classes = (IsAuthenticated,)
