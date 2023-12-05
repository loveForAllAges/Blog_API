from django.urls import path, include
from .views import *


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('login', CustomAuthToken.as_view()),
    path('users', UserListAPIView.as_view())
]
