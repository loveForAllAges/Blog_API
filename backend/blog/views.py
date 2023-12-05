from rest_framework import viewsets
from rest_framework. permissions import IsAuthenticated

from .models import Blog
from .serializer import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Blog.objects.filter(user=self.request.user)
        return queryset
