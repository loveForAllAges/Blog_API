from rest_framework import viewsets, generics
from rest_framework. permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Blog, Tag
from .serializers import BlogSerializer, TagSerializer
from .pagination import CustomCursorPagination


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter]
    search_fields = ('title', 'content')
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Blog.objects.filter(user=self.request.user)
        return queryset


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class HomeListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomCursorPagination
    # TODO ПОИСК, СОРТИРОВКА ПО ТЕГАМ


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     serializer = self.get_serializer(page, many=True)
    #     data = {
    #         'next': self.paginator.get_next_link(),
    #         'blogs': serializer.data,
    #         'authors': get_users(),
    #         'get_tags': get_tags(),
    #     }
    #     return Response(data)
