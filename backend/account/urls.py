from django.urls import path, include
from .views import *


urlpatterns = [
    path('login', LoginAPIView.as_view()),
    path('signup', SignupAPIView.as_view()),
]
