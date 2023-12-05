from django.urls import path
from .views import *


urlpatterns = [
    path('login', CustomAuthToken.as_view()),
    path('users', UserListAPIView.as_view())
]
