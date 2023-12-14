from django.db import models
from django.conf import settings

import uuid


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=128)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
