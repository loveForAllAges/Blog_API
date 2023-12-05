from django.db import models
from django.conf import settings


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
