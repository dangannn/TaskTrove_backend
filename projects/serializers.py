from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from projects.models import Project, ProjectRequest


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'urgency', 'payment', 'customer', 'freelancer', 'pub_date']

    def validate_payment(self, value):
        """
        Проверка валидности поля "payment".
        """
        if value < 0:
            raise serializers.ValidationError("Оплата не может быть отрицательной.")
        return value


class ProjectRequestSerializer(ModelSerializer):
    class Meta:
        model = ProjectRequest
        fields = ['id', 'name', 'description', 'customer', 'freelancer', 'pub_date']
