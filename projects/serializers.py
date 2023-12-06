from rest_framework.serializers import ModelSerializer

from projects.models import Project, ProjectRequest


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'urgency', 'payment', 'customer', 'freelancer', 'pub_date']


class ProjectRequestSerializer(ModelSerializer):
    class Meta:
        model = ProjectRequest
        fields = ['id', 'name', 'description', 'customer', 'freelancer', 'pub_date']
