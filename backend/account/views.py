from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import views, generics

from .serializers import UserDetailSeralizer, SignupSerializer

from django.contrib.auth import get_user_model


User = get_user_model()


class LoginAPIView(ObtainAuthToken):
    pass


class SignupAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all().prefetch_related('blogs')
    serializer_class = UserDetailSeralizer
    lookup_field = 'username'

    def update(self, request, *args, **kwargs):
        res = {'message': 'Ошибка.'}
        if request.user.is_authenticated:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            if request.user == instance:
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                if getattr(instance, '_prefetched_objects_cache', None):
                    instance._prefetched_objects_cache = {}
                res = serializer.data
        return Response(res)
