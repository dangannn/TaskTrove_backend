from django.db import models
from simple_history.models import HistoricalRecords

from users.models import CustomUser


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='comment_author')
    pub_date = models.DateTimeField(auto_now_add=True)
    is_positive = models.BooleanField(blank=False, default=True)
    description = models.CharField(max_length=1000, null=True)
    freelancer = models.ManyToManyField(CustomUser, related_name='freelancer_comments', blank=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.description


class FavoriteList(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='favorite_list')
    freelancer = models.ManyToManyField(CustomUser, related_name='freelancer_favorite_list', blank=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Список избранных"
        verbose_name_plural = "Списки избранных"
