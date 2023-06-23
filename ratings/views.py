from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.serializers import ProjectSerializer
from ratings.models import Comment, FavoriteList
from ratings.serializers import CommentSerializer, FavoriteListSerializer
from users.serializers import FreelancerSerializer, CustomerSerializer


class CommentsView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # permission_classes = (IsAuthenticated,)



class FavoriteListsView(ModelViewSet):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer

    # permission_classes = (IsAuthenticated,)

    # вывод favorite_list
    @action(detail=True, methods=['get'], name='favorite_list', url_path='favorite_list')
    def favorite_list(self, request, pk):
        user_id: int = int(pk)
        queryset = self.get_queryset().filter(customer=user_id)[0].freelancer
        # serializer = FreelancerSerializer(queryset, many=True)
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], name='update_favorite_list', url_path='update_favorite_list')
    def add_freelancer(self, request, pk, *args, **kwargs):
        user_id = int(pk)
        # Получаем объект пользователя, которого нужно обновить
        instance = self.get_queryset().filter(customer=user_id)[0]
        partial = kwargs.pop('partial', False)
        request.data['freelancer'] += [_['id'] for _ in [*instance.freelancer.values()]]

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # Если 'prefetch_related' был применен к queryset, нужно явно сбросить кэш prefetch на объекте.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=True, methods=['patch'], name='remove_favorite_list', url_path='remove_favorite_list')
    def remove_freelancer(self, request, pk, *args, **kwargs):
        user_id = int(pk)
        # Получаем объект пользователя, которого нужно обновить
        instance = self.get_queryset().filter(customer=user_id)[0]
        partial = kwargs.pop('partial', False)
        tmp_data = [_['id'] for _ in [*instance.freelancer.values()]]
        tmp_data.remove(request.data['freelancer'][0])
        request.data['freelancer'] = tmp_data

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # Если 'prefetch_related' был применен к queryset, нужно явно сбросить кэш prefetch на объекте.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
