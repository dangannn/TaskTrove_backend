from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):
    # def create(self, validated_data):
    #     user = CustomUser(**validated_data)
    #
    #     user.set_password(validated_data["password"])
    #     user.save()
    #
    #     return user
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', [])  # Извлекаем группы из валидированных данных

        user = CustomUser.objects.create(**validated_data)
        if password:
            user.set_password(password)  # Хэширование пароля
            user.save()

        user.groups.set(groups)  # Устанавливаем связи между пользователем и группами

        return user

    class Meta:
        model = CustomUser
        fields = ['id', "first_name", "last_name", 'username', 'password', 'email', 'groups', 'phone_number']


class FreelancerSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", 'email', 'phone_number']
