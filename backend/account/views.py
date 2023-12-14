from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import views, generics, status, permissions

from .serializers import UserDetailSerializer, SignupSerializer

from django.contrib.auth import get_user_model


User = get_user_model()


class LoginAPIView(ObtainAuthToken):
    pass


class LogoutAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.user.auth_token)
        request.user.auth_token.delete()
        return Response({'message': 'Вы вышли из системы.'}, status=status.HTTP_200_OK)


class SignupAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all().prefetch_related('blogs')
    serializer_class = UserDetailSerializer
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
