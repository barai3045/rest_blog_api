from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    post_date = serializers.DateField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)