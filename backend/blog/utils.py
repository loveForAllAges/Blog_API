from django.contrib.auth import get_user_model

from .models import Tag


def get_tags():
    queryset = Tag.objects.all()
    return queryset


def get_users(request):
    queryset = get_user_model().objects.exclude(id=request.user.id)
    return queryset
