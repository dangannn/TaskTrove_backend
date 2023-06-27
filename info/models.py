from django.db import models

from users.models import CustomUser


# Create your models here.
class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='news')
    pub_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name
