from rest_framework import serializers

from . import models



class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reader
        fields = '__all__'
        depth = 2


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Story
        fields = '__all__'
        depth = 1


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['content', 'role']