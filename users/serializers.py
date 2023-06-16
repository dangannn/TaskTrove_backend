from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', "first_name", "last_name", 'username', 'password', 'email', 'groups']


class FreelancerSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]
