from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser
from users.serializers import UserSerializer


class UsersView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
