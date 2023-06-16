from django.db import models

from users.models import CustomUser


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='comment_author')
    description = models.CharField(max_length=1000, null=True)
    freelancer = models.ManyToManyField(CustomUser, related_name='freelancer_comments')

    def __str__(self):
        return self.description
