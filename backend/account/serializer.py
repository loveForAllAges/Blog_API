from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from .validators import validate_username


class UserSerializer(serializers.ModelSerializer):
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
        # password = validated_data.pop('password')
        instance = self.Meta.model.objects.create_user(**validated_data)
        # instance.
        return instance
