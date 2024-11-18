from rest_framework import serializers
from .models import CustomUser, Channel, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'is_moderator')

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
