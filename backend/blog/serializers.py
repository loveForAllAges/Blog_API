from rest_framework import serializers

from .models import Blog, Tag
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, allow_empty=False)

    class Meta:
        model = Blog
        fields = ('title', 'content', 'tags', 'url')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        request = self.context.get('request')
        validated_data['user'] = request.user
        instance = self.Meta.model.objects.create(**validated_data)
        instance.tags.set(tags)
        return instance
