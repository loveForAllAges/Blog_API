from rest_framework import viewsets, generics
from rest_framework. permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Blog, Tag
from .serializers import BlogSerializer, TagSerializer
from .pagination import CustomCursorPagination
from .permissions import IsAuthor
from .filters import BlogFilter


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    queryset = Blog.objects.all().select_related('user')
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    filterset_class = BlogFilter
    search_fields = ('title', 'content',)
    serializer_class = BlogSerializer
    pagination_class = CustomCursorPagination


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
