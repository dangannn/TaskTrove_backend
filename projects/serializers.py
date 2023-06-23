from rest_framework.serializers import ModelSerializer

from projects.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'customer', 'freelancer', 'pub_date']


class ProjectRequestSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'customer', 'freelancer', 'pub_date']
