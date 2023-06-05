from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectsView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, )
