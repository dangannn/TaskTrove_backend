from datetime import datetime, timedelta
from django.utils import timezone

from django.db.models import Q
from rest_framework import status, filters
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

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['pub_date', 'payment', 'urgency']

    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'], name='projects', url_path='projects')
    def projects_list(self, request, pk):
        user_id: int = int(pk)  # Получение значения аргумента id из pk
        queryset = self.get_queryset()
        queryset = queryset.filter(customer=user_id)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], name='best_week_projects', url_path='best_week_projects')
    def best_week_projects(self, request):
        queryset = self.get_queryset()
        current_date = timezone.now().date()
        start_of_next_week = current_date + timedelta(days=(6 - current_date.weekday()) + 1)
        queryset = queryset.filter(
            Q(pub_date__gte=current_date - timedelta(days=7)) & ((
                    Q(urgency__lte=start_of_next_week) & ~Q(payment__lte=100000) |
                    Q(urgency__gte=start_of_next_week) & Q(payment__lte=100000))
            ))
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], name='best_year_projects', url_path='best_year_projects')
    def best_year_projects(self, request):
        queryset = self.get_queryset()
        current_date = timezone.now().date()
        start_of_next_year = current_date.replace(year=current_date.year + 1, month=1, day=1)
        queryset = queryset.filter(
            Q(pub_date__gte=current_date - timedelta(days=365)) & ((
                    Q(urgency__lte=start_of_next_year) & ~Q(payment__lte=100000) |
                    Q(urgency__gte=start_of_next_year) & Q(payment__lte=100000) & Q(payment__gte=10000))
            ))
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='freelancers_list', url_path='freelancers')
    def freelancers_list(self, request, pk):
        project_id: int = int(pk)
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
