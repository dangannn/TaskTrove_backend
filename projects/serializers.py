from rest_framework.serializers import ModelSerializer

from projects.models import Project
from users.serializers import UserSerializer


class ProjectSerializer(ModelSerializer):
    # users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ['name', 'description', 'customer']
