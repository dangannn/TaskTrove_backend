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
        # queryset = queryset[user_id].freelancer_projects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['patch'], name='remove_project', url_path='remove_project')
    # def remove_project(self, request, pk, *args, **kwargs):
    #     user_id = int(pk)
    #     # Получаем объект пользователя, которого нужно обновить
    #     instance = self.get_queryset().filter(customer=user_id)[0]
    #     partial = kwargs.pop('partial', False)
    #     tmp_data = [_['id'] for _ in [*instance.freelancer.values()]]
    #     tmp_data.remove(request.data['freelancer'][0])
    #     request.data['freelancer'] = tmp_data
    #
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # Если 'prefetch_related' был применен к queryset, нужно явно сбросить кэш prefetch на объекте.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)

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

    permission_classes = (IsAuthenticated,)
