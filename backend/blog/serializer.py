from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'content')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        instance = self.Meta.model.objects.create(**validated_data)
        return instance