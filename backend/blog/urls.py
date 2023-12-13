from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'tag', TagViewSet, basename='tag')


urlpatterns = [
    path('home', HomeListAPIView.as_view()),
    path('', include(router.urls)),
]
