from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Blog, Tag


User = get_user_model()
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user', lookup_field='username')

    class Meta:
        model = User
        exclude = ('password',)


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, allow_empty=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        exclude = ('created', )
        # fields = ('title', 'content', 'updated', 'tags', 'user')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        request = self.context.get('request')
        validated_data['user'] = request.user
        instance = self.Meta.model.objects.create(**validated_data)
        instance.tags.set(tags)
        return instance
