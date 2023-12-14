from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from .validators import validate_username
from blog.serializers import BlogSerializer


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[validate_username, UniqueValidator(User.objects.all(), 'Имя пользователя занято.')],
        error_messages={
            'blank': 'Это обязательное поле.',
        },
    )
    password = serializers.CharField(error_messages={
        'blank': 'Это обязательное поле.',
    })

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        instance = self.Meta.model.objects.create_user(**validated_data)
        return instance


class UserDetailSeralizer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user', lookup_field='username')
    blogs = BlogSerializer(read_only=True, many=True)

    class Meta:
        model = User
        exclude = ('password',)

    def update(self, instance, validated_data):
        print(instance, validated_data)
        return super().update(instance, validated_data)